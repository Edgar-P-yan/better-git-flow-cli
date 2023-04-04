"""
Helpers for unit tests
"""

import sys
import importlib
import os


def import_path(path):
    """
    Imports any python module, regardless it's name, location,
    file extension and etc. Used to import git-flow file in unit tests.
    """
    module_name = os.path.basename(path).replace('-', '_')
    spec = importlib.util.spec_from_loader(
        module_name,
        importlib.machinery.SourceFileLoader(module_name, path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module


class Case:
    """
    A wrapper for unit test cases.
    """
    input = None
    want = None

    def __init__(self, _input, want) -> None:
        self.input = _input
        self.want = want
