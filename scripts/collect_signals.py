from typing import Dict, Type

import importlib, json, pathlib

from PySide6.QtCore import Signal

JSON_OUTPUT_FNAME = pathlib.Path(__file__).parent / 'class-signals.json'

def collect_class_signals_for_module(module_name: str, d: Dict[str, str]) -> None:
    '''Load module, inspect all attribute types and fill dict with signals one'''
    if module_name.startswith('_'):
        return

    print('Processing %s' % module_name)
    try:
        m = importlib.import_module(f'PySide6.{module_name}')
    except ModuleNotFoundError:
        print('... Module not available!')
        # platform-specific modules can not be imported for example on other platforms
        return

    for class_name, class_type in m.__dict__.items():
        if class_name.startswith('_'):
            continue

        collect_class_signals_for_class(f'{module_name}.{class_name}', class_type, d)

def collect_class_signals_for_class(class_fqn: str, class_type: Type, d: Dict[str, str]) -> None:
    # we only care about classes
    try:
        class_members = class_type.__dict__.items()
    except AttributeError:
        # this is not a class
        return

    for class_attr_name, class_attr_value in class_members:
        if class_attr_name.startswith('_'):
            continue

        # tricky way to find an instance of Shiboken.EnumType
        if isinstance(class_attr_value, Signal):
            d[class_fqn] = d.get(class_fqn, list())
            d[class_fqn].append(class_attr_name)
        else:
            collect_class_signals_for_class(f'{class_fqn}.{class_attr_name}', class_attr_value, d)


def main():
    d = {}
    for fpath in (pathlib.Path(__file__).parent.parent / 'PySide6-stubs').glob('*.pyi'):
        module_name = fpath.stem
        collect_class_signals_for_module(module_name, d)

    with open(JSON_OUTPUT_FNAME, 'w') as f:
        json.dump(d, f, indent=4)



if __name__ == '__main__':
    main()