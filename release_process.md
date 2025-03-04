Instructions for a new release:

- update version in setup.cfg
- update version in version.py
- python -m build --wheel .
- python -m build --sdist .
- twine upload dist\pyside6_stubs-6.7.3.0.tar.gz dist\pyside6_stubs-6.7.3.0-py3-none-any.whl

