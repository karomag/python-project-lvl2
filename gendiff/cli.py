# -*- coding: utf-8 -*-

"""Generate diff."""

import argparse
import json
import sys
from os import path


def parse_args():
    """Parse arguments.

    Automatically generate help and usage messages.

    Returns:
        option: Inspect the command line, convert each argument
                to the appropriate type.
    """
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    group = parser.add_argument_group('format settings')
    group.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def _get_dic_from_file(path_to_file):
    with open(path.abspath(path_to_file)) as inf:
        return json.load(inf)


def _modify_keys(input_set, symbol=' '):
    temp_dic = {}
    for element in input_set:
        key, value = element
        temp_dic[symbol + ' ' + key] = value
    return temp_dic


def generate_diff(path_to_file_before, path_to_file_after):
    """Find differences in files.

    Args:
        path_to_file_before: path to file1
        path_to_file_after: path to file2

    Returns:
        file1, file2
    """
    file_before = _get_dic_from_file(path_to_file_before)
    file_after = _get_dic_from_file(path_to_file_after)
    set_keys_before = set(file_before.items())
    set_keys_after = set(file_after.items())
    diff_dic = {}
    diff_dic.update(_modify_keys(set_keys_after - set_keys_before, '+'))
    diff_dic.update(_modify_keys(set_keys_before - set_keys_after, '-'))
    diff_dic.update(dict(set_keys_before & set_keys_after))
    print(diff_dic)

    return set_keys_before, set_keys_after
