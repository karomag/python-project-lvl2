# -*- coding: utf-8 -*-

"""Generate diff."""

import json
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


def check_key(key, diff, before_dict, after_dict):
    """Check key for change.

    Args:
        key: current key
        diff: dictionary
        before_dict: before data
        after_dict:  after data
    """
    set1 = set(before_dict.keys())
    set2 = set(after_dict.keys())
    before_value = before_dict.get(key)
    after_value = after_dict.get(key)
    # set1 & set2
    if key in set2 & set1:
        if before_value == after_value:
            diff[(key, 'old')] = before_value
        else:
            diff[(key, 'deleted')] = before_value
            diff[(key, 'added ')] = after_value
    # set1 - set2
    if key in set1 - set2:
        diff[(key, 'deleted')] = before_value
    # set2 - set1
    if key in set2 - set1:
        diff[(key, 'added')] = after_value


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
        are_children = (
            isinstance(before_dict.get(key), dict)
        ) and (
            isinstance(after_dict.get(key), dict)
        )
        if are_children:
            add_node(
                diff.setdefault((key, 'old'), {}),
                before_dict.get(key),
                after_dict.get(key),
            )
        else:
            check_key(key, diff, before_dict, after_dict)


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

    diff = {}
    add_node(diff, before_dict, after_dict)
    diff_string = json.dumps(diff, sort_keys=True, indent=2)

    return diff_string.replace('"', '')
