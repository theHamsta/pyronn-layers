# -*- coding: utf-8 -*-
#
# Copyright © 2019 Stephan Seitz <stephan.seitz@fau.de>
#
# Distributed under terms of the GPLv3 license.

"""

"""
import importlib.util
import sys
from glob import glob
from os.path import basename, dirname, join

import pytest

example_files_glob = join(dirname(__file__), 'PYRO-NN', 'examples', '**', '*.py')
example_files = glob(example_files_glob, recursive=True)

sys.path.append(join(dirname(__file__), 'PYRO-NN'))
sys.path.append(join(dirname(__file__), 'PYRO-NN', 'example_learning_tensorflow'))


@pytest.mark.parametrize('file', example_files)
def test_pyronn_examples(file):

    for file in example_files:
        spec = importlib.util.spec_from_file_location(basename(file), file)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
