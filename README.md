This is an MVCE for a bug in [Hatch](https://hatch.pypa.io), in which building
a wheel with a custom build hook that force-includes a file with a path that
would normally already be in the wheel results in a warning from Python and an
invalid wheel.

To use this MVCE, run `python3 -m build` or `python3 -m build --wheel` and
observe that the resulting `dist/*.whl` file contains two
`mypackage/__init__.py` files and the `*.dist-info/RECORD` file lists
`mypackage/__init__.py` twice with different hashes.

The bug report is at <https://github.com/pypa/hatch/issues/1030>.
