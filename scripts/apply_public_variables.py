from typing import Dict, Optional, Union

import pathlib
import json

import libcst
import libcst as cst
import libcst.matchers as matchers

JSON_INPUT_FNAME = pathlib.Path(__file__).parent / 'public-variables.json'


class TypingTransformer(cst.CSTTransformer):
    """TypingTransformer that visits classes and methods."""

    def __init__(self, mod_name: str, d: Dict[str, str]) -> None:
        super().__init__()
        self.mod_name = mod_name
        self.full_name_stack = [mod_name]
        self.fqn_class_pub_var = d
        self.visited_attributes = []

    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        """Put a class on top of the stack when visiting."""
        self.full_name_stack.append(node.name.value)
        return True

    def leave_AnnAssign(self, original_node: cst.AnnAssign, updated_node: cst.AnnAssign) \
            -> cst.AnnAssign:
        fqn_class = '.'.join(self.full_name_stack)
        if fqn_class not in self.fqn_class_pub_var:
            return updated_node

        attr_ann_type_dict = self.fqn_class_pub_var[fqn_class]
        attr_name = original_node.target.value
        self.visited_attributes.append(attr_name)
        if attr_name not in attr_ann_type_dict:
            # we have no info about this attribute
            return updated_node

        ann_value = original_node.annotation.annotation.value
        if ann_value == attr_ann_type_dict[attr_name]:
            # we agree with annotation
            return updated_node

        # let's update the annotation
        print(f'Fixing {fqn_class}.{attr_name} from annotation "{ann_value}" to "{attr_ann_type_dict[attr_name]}"')
        annotation = updated_node.annotation.with_changes(
            annotation=type_to_expression(attr_ann_type_dict[attr_name])
        )
        return updated_node.with_changes(annotation=annotation)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) \
            -> Union[cst.BaseStatement, cst.FlattenSentinel[cst.BaseStatement], cst.RemovalSentinel, ]:
        fqn_class = '.'.join(self.full_name_stack)
        self.full_name_stack.pop()

        # no variables to adjust
        if fqn_class not in self.fqn_class_pub_var:
            return updated_node

        attr_ann_type_dict = self.fqn_class_pub_var[fqn_class]

        nonAnnotatedAttributes = set()

        for class_content in updated_node.body.body:
            if matchers.matches(class_content, matchers.SimpleStatementLine(body=[matchers.Assign()])):
                nonAnnotatedAttributes.add(class_content.body[0].targets[0].target.value)


        missingPubVar = sorted(set(attr_ann_type_dict.keys()) - nonAnnotatedAttributes - set(self.visited_attributes))

        if not missingPubVar:
            # all public variables are already there
            return updated_node

        pre_body = []
        for pub_var in missingPubVar:
            print(f'Class {fqn_class}: adding public variable {pub_var}: {attr_ann_type_dict[pub_var]}')
            pre_body.append(libcst.parse_statement(f'{pub_var}: {attr_ann_type_dict[pub_var]}'))
        pre_body.insert(0, libcst.EmptyLine(indent=False, newline=libcst.Newline()))
        pre_body.append(libcst.EmptyLine(indent=False, newline=libcst.Newline()))

        if isinstance(updated_node.body, libcst.SimpleStatementSuite):
            # the class is a single ellipsis, we need to create a full indented body
            return updated_node.with_changes(
                body=libcst.IndentedBlock(body=pre_body)
            )

        # regular class
        return updated_node.with_changes(
            body=updated_node.body.with_changes(
                body=tuple(pre_body) + updated_node.body.body
            )
        )


def type_to_expression(typ: str) -> cst.BaseExpression:
    if '.' not in typ:
        return cst.Name(typ)
    left, right = typ.rsplit('.', 1)
    return cst.Attribute(
        value=type_to_expression(left), attr=cst.Name(right)
    )


def apply_public_variables_for_module(module_path: str, d: Dict[str, str]) -> None:
    if module_path.name.startswith('_'):
        return

    module_name = module_path.stem

    print('Fixing ', module_name)
    with open(module_path, "r", encoding="utf-8") as fhandle:
        stub_tree = cst.parse_module(fhandle.read())

    transformer = TypingTransformer(module_name, d)
    modified_tree = stub_tree.visit(transformer)

    with open(module_path, "w", encoding="utf-8") as fhandle:
        fhandle.write(modified_tree.code)


def main():
    with open(JSON_INPUT_FNAME, 'r') as f:
        d = json.load(f)

    for fpath in (pathlib.Path(__file__).parent.parent / 'PySide6-stubs').glob('*.pyi'):
        apply_public_variables_for_module(fpath, d)



if __name__ == '__main__':
    # auto_test()
    main()
