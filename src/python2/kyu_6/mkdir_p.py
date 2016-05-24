# coding=utf-8

"""mkdir -p
http://www.codewars.com/kata/mkdir-p

Write a synchronous function that makes a directory and recursively makes all
of its parent directories as necessary.

A directory is specified via a sequence of arguments which specify the path.
For example:

    mkdirp('/','tmp','made','some','dir')

...will make the directory /tmp/made/some/dir.

Like the shell command mkdir -p, the function you program should be idempotent
if the directory already exists.
"""

import os


def mkdirp(*directories):
    """Recursively create all directories as necessary

    Args:
        directories (tuple): List of directories

    Returns:
        None
    """
    try:
        os.makedirs(os.path.join(*directories))
    except OSError:
        pass
