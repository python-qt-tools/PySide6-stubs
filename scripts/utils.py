import pathlib
from typing import Union, Dict, Optional

import libcst as cst


def resolve_cst_attr(node: Union[cst.Name, cst.Attribute, cst.Subscript, cst.SubscriptElement, cst.Index]) -> str:
    '''Return a string from an annotation node'''
    if isinstance(node, cst.Name):
        return node.value

    if isinstance(node, cst.Attribute):
        return f'{resolve_cst_attr(node.value)}.{resolve_cst_attr(node.attr)}'

    if isinstance(node, cst.Subscript):
        return f'{resolve_cst_attr(node.value)}[{", ".join(resolve_cst_attr(el) for el in node.slice)}]'

    if isinstance(node, cst.SubscriptElement):
        return resolve_cst_attr(node.slice)

    if isinstance(node, cst.Index):
        return resolve_cst_attr(node.value)

    if isinstance(node, cst.SimpleString):
        return node.value

    if isinstance(node, cst.Call):
        return f'{resolve_cst_attr(node.func)}({", ".join(resolve_cst_attr(arg) for arg in node.args)})'

    if isinstance(node, cst.Arg):
        return resolve_cst_attr(node.value)

    raise ValueError('Unknown type: ', type(node))


def self_test():
    assert resolve_cst_attr(cst.parse_expression('PySide6.QtGui.QCursor')) == 'PySide6.QtGui.QCursor'
    assert resolve_cst_attr(cst.parse_expression('PySide6.QtGui.QCursor  ')) == 'PySide6.QtGui.QCursor'
    assert resolve_cst_attr(cst.parse_expression('Union[PySide6.QtGui.QCursor] ')) == 'Union[PySide6.QtGui.QCursor]'
    assert resolve_cst_attr(cst.parse_expression('Union[PySide6.QtGui.QCursor ] ')) == 'Union[PySide6.QtGui.QCursor]'
    assert resolve_cst_attr(cst.parse_expression('Union[PySide6.QtGui.QCursor, aa.bb ] ')) == 'Union[PySide6.QtGui.QCursor, aa.bb]'
    print('Self-test: OK')


class FixAutoConversionTypingTransformer(cst.CSTTransformer):
    """TypingTransformer that visits classes and methods."""

    def __init__(self, mod_name: str, d: Dict[str, str], target_annotation, replacement_annotation) -> None:
        super().__init__()
        self.full_name_stack = [mod_name]
        self.d = d
        self.target_annotation = target_annotation
        self.replacement_annotation = replacement_annotation

    def fqn_name(self) -> str:
        return '.'.join(self.full_name_stack)


    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        """Put a class on top of the stack when visiting."""
        self.full_name_stack.append( node.name.value )
        return True

    def visit_FunctionDef(self, node: cst.FunctionDef) -> Optional[bool]:
        # search for all arguments with type annotation
        self.full_name_stack.append( node.name.value )


    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) -> None:
        fqn_name = self.fqn_name()
        self.full_name_stack.pop()

        for i, param in enumerate(updated_node.params.params):
            fqn_param = '%s().%s' % (fqn_name, param.name.value)
            fqn_annotation = ''
            if param.annotation:
                fqn_annotation = resolve_cst_attr(param.annotation.annotation)
            if (fqn_annotation == self.target_annotation):
                self.d['collected'][fqn_param] = 'QCursor'
                # print('Node before: ', updated_node)
                print('Fixing: ', fqn_param, fqn_annotation)
                updated_node = updated_node.with_changes(
                                    params=updated_node.params.with_changes(
                                            params=updated_node.params.params[:i]
                                            + (updated_node.params.params[i].with_changes(annotation=cst.Annotation(annotation=cst.parse_expression(self.replacement_annotation))),)
                                            + updated_node.params.params[i+1:]
                    )
                )
                # print('Node after: ', updated_node)
                self.d['fixed'][fqn_param] = 'QCursor'

        return updated_node



    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) \
            -> Union[cst.BaseStatement, cst.FlattenSentinel[cst.BaseStatement], cst.RemovalSentinel,]:
        """Remove a class from the stack and return the updated node."""
        self.full_name_stack.pop()
        return updated_node


def fix_auto_conversion_for_module(module_path: pathlib.Path, d: Dict[str, str], target_annotation, replacement_annotation) -> None:
    '''Load module, inspect all QFlags types and fill dict with the information'''
    module_name = module_path.stem
    if module_name.startswith('_'):
        return

    print('Processing %s' % module_name)
    if module_name.startswith('_'):
        return

    with open(module_path, "r", encoding="utf-8") as fhandle:
        stub_tree = cst.parse_module(fhandle.read())

    transformer = FixAutoConversionTypingTransformer(module_name, d, target_annotation, replacement_annotation)
    modified_tree = stub_tree.visit(transformer)

    with open(module_path, "w", encoding="utf-8") as fhandle:
        fhandle.write(modified_tree.code)