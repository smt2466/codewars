# coding=utf-8
# pylint: disable=missing-docstring

"""
mkdir -p
"""

import os
import pytest

from src.kyu_6.mkdir_p import mkdirp


def test_creates_directories(tmpdir):
    path = [str(tmpdir), "directories", "can", "be", "made", "recursively"]
    mkdirp(*path)
    assert os.path.exists(os.path.join(*path))


def test_path_already_exists(tmpdir):
    path = str(tmpdir)
    try:
        mkdirp(*path)
    except OSError:
        pytest.fail('mkdirp raises error for existed directory')

