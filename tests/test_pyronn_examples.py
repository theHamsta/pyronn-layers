# -*- coding: utf-8 -*-
#
# Copyright © 2019 Stephan Seitz <stephan.seitz@fau.de>
#
# Distributed under terms of the GPLv3 license.

"""

"""
import importlib.util
from glob import glob
from os.path import basename, dirname, join


def test_pyronn_examples():
    example_files_glob = join(dirname(__file__), 'PYRO-NN', 'examples', '**', '*.py')
    example_files = glob(example_files_glob, recursive=True)

    for file in example_files:
        print(file)
        print(basename(file))
        spec = importlib.util.spec_from_file_location(basename(file), file)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)


