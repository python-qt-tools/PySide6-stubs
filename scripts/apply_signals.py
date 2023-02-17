from typing import Dict, Optional, Union

import pathlib, json

import libcst
import libcst as cst
import libcst.matchers as matchers

JSON_INPUT_FNAME = pathlib.Path(__file__).parent / 'class-signals.json'

class TypingTransformer(cst.CSTTransformer):
    """TypingTransformer that visits classes and methods."""

    def __init__(self, mod_name: str, d: Dict[str, str]) -> None:
        super().__init__()
        self.mod_name = mod_name
        self.full_name_stack = [mod_name]
        self.fqn_class_signals = d
        self.annotation = []


    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        """Put a class on top of the stack when visiting."""
        self.full_name_stack.append( node.name.value )
        return True


    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) \
            -> Union[cst.BaseStatement, cst.FlattenSentinel[cst.BaseStatement], cst.RemovalSentinel, ]:
        fqn_class = '.'.join(self.full_name_stack)
        self.full_name_stack.pop()

        # no signals to adjust
        if not fqn_class in self.fqn_class_signals:
            return updated_node

        collected_signals = set(self.fqn_class_signals[fqn_class])

        nonAnnotatedAttributes = set()
        annotatedAttributes = set()

        for class_content in updated_node.body.body:
            if matchers.matches(class_content, matchers.SimpleStatementLine(body=[matchers.Assign()])):
                nonAnnotatedAttributes.add(class_content.body[0].targets[0].target.value)

            if matchers.matches(class_content, matchers.SimpleStatementLine(body=[matchers.AnnAssign()])):
                annotatedAttributes.add(class_content.body[0].target.value)

        missingSignals = sorted(collected_signals - nonAnnotatedAttributes - annotatedAttributes)

        if not missingSignals:
            # all signals are already there
            return updated_node

        pre_body = []
        for signal in missingSignals:
            print(f'Class {fqn_class}: adding signal {signal}')
            pre_body.append(libcst.parse_statement(f'{signal}: PySide6.QtCore.Signal'))
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


def apply_signals_for_module(module_path: str, d: Dict[str, str]) -> None:
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
        apply_signals_for_module(fpath, d)



if __name__ == '__main__':
    # auto_test()
    main()
