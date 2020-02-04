# -*- coding: utf-8 -*-

"""Generate diff."""

from collections import defaultdict
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


def add_node(diff, before_dict, after_dict):
    """Add node in diff.

    Args:
        diff: dictionary
        before_dict: before data
        after_dict:  after data
    """
    set1 = set(before_dict.keys())
    set2 = set(after_dict.keys())
    for key in set1 | set2:
        before_value = before_dict.get(key)
        after_value = after_dict.get(key)

        # set1 & set2
        if isinstance(before_value, dict) and isinstance(after_value, dict):
            add_node(diff[key], before_value, after_value)
        if before_value == after_value:
            diff[(key, '   ')] = before_value
        else:
            diff[(key, ' - ')] = before_value
            diff[(key, ' + ')] = after_value
            
        # set1 - set2
        if key in before_dict and key not in after_dict:
            diff[(key, ' - ')] = before_value
            continue
        # set2 - set1
        if key not in before_dict and key in after_dict:
            diff[(key, ' + ')] = after_value
            continue


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
