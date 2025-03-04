from typing import Dict, Type

import importlib, json, pathlib

from PySide6.QtWidgets import QApplication

JSON_OUTPUT_FNAME = pathlib.Path(__file__).parent / 'public-variables.json'

RESERVED_KEYWORDS = [
    'from',
    'QRhiResource',
    'QRhiTexture',
    'QRhiBuffer',
    'QRhiSampler',
    'QRhiShaderResourceBinding',
    'QTimeZone',
]

def collect_public_variables_for_module(module_name: str, d: Dict[str, str]) -> None:
    '''Load module, inspect all attribute types and fill dict with information'''
    if module_name.startswith('_'):
        return

    print('Processing %s' % module_name)
    try:
        m = importlib.import_module(f'PySide6.{module_name}')
    except (ModuleNotFoundError, ImportError):
        print('... Module not available!')
        # platform-specific modules can not be imported for example on other platforms
        return

    module_attributes = set(dir(m)) | set(m.__dict__.keys())
    for class_name in module_attributes:
        if class_name.startswith('_'):
            continue

        if class_name in RESERVED_KEYWORDS:
            continue

        class_type = getattr(m, class_name)
        print(f'collecting {module_name}.{class_name}')
        collect_public_variables_for_class(f'{module_name}.{class_name}', class_type, d)


def collect_public_variables_for_class(class_fqn: str, class_type: Type, d: Dict[str, str]) -> None:
    # we only care about classes
    #print(f'trying to access {class_fqn}.__dict__ for {type(class_type)}')
    try:
        class_members = class_type.__dict__.items()
    except AttributeError:
        # this is not a class
        return

    #print(f'Iterating class members of {class_fqn}')
    instance = None
    for class_attr_name, class_attr_value in class_members:
        if class_attr_name.startswith('_'):
            continue

        if class_attr_name in RESERVED_KEYWORDS:
            continue

        if class_attr_value.__class__.__name__ in ('getset_descriptor', 'method_descriptor'):

            # create the instance on-demand
            if instance is None:
                try:
                    instance = class_type()
                except Exception:
                    # we can not work without the instance
                    return

            attr_of_instance = getattr(instance, class_attr_name)
            if attr_of_instance == None:
                continue
            typename = attr_of_instance.__class__.__qualname__
            modulename = attr_of_instance.__class__.__module__
            if modulename != "builtins":
                typename = f'{modulename}.{typename}'

            try:
                pub_var_dict = d[class_fqn]
            except KeyError:
                pub_var_dict = {}
                d[class_fqn] = pub_var_dict
            pub_var_dict[class_attr_name] = typename
        else:
            # try if it is a subclass
            collect_public_variables_for_class(f'{class_fqn}.{class_attr_name}', class_attr_value, d)


def main():
    application = QApplication(['-platform', 'minimal'])    # needed for instancing QWidgets
    d = {}
    for fpath in (pathlib.Path(__file__).parent.parent / 'PySide6-stubs').glob('QtNfc.pyi'):
        module_name = fpath.stem
        collect_public_variables_for_module(module_name, d)

    with open(JSON_OUTPUT_FNAME, 'w') as f:
        json.dump(d, f, indent=4)



if __name__ == '__main__':
    main()