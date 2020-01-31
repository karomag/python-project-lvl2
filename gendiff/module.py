# -*- coding: utf-8 -*-

"""Generate diff."""

from os import path
from collections import defaultdict

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


def add_node(diff, before_dict, after_dict):
    """"""
    data = before_dict.keys() | after_dict.keys()
    for key in data:
        if key in before_dict and key not in after_dict:
            diff[key] = {
                'state': 'deleted',
                'value': before_dict[key],
            }
        elif key not in before_dict and key in after_dict:
            diff[key] = {
                'state': 'added',
                'value': after_dict[key],
            }
        else:
            if isinstance(before_dict[key], dict) and isinstance(after_dict[key], dict):
                add_node(diff[key], before_dict[key], after_dict[key])
            elif before_dict[key] != after_dict[key]:
                diff[key] = {
                    'state': 'old',
                    'value': before_dict[key],
                }
            else:
                diff[key] = {
                    'state': 'old',
                    'value': before_dict[key],
                }


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

    diff = defaultdict(dict)
    add_node(diff, before_dict, after_dict)

    return diff
