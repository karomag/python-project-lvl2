# -*- coding: utf-8 -*-

"""Generate diff."""

from os import path

from gendiff.parsers import parse_file


def read_file(path_to_file):
    """Read file.

    Args:
        path_to_file: file to loading

    Returns:
        dictionary
    """
    with open(path.abspath(path_to_file)) as inf:
        return parse_file(
            inf.read(),
            path.splitext(path.basename(path_to_file))[1],
        )


def generate_diff(path_to_file_before, path_to_file_after):
    """Find differences in files.

    Args:
        path_to_file_before: path to file1
        path_to_file_after: path to file2

    Returns:
        str; diff string
    """
    before_dict = read_file(path_to_file_before)
    after_dict = read_file(path_to_file_after)

    return before_dict.keys() | after_dict.keys()
