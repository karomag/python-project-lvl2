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


def _get_set_from_json(path_to_file):
    with open(path.abspath(path_to_file)) as inf:
        return set(json.load(inf).items())


def _modify_keys(input_set, symbol=' '):
    temp_dic = {}
    for element in input_set:
        key, value_dic = element
        temp_dic['{0} {1}'.format(symbol, key)] = value_dic
    return temp_dic


def generate_diff(path_to_file_before, path_to_file_after):
    """Find differences in files.

    Args:
        path_to_file_before: path to file1
        path_to_file_after: path to file2

    Returns:
        file1, file2
    """
    set_items_before = _get_set_from_json(path_to_file_before)
    set_items_after = _get_set_from_json(path_to_file_after)
    diff_dic = {}
    diff_dic.update(_modify_keys(set_items_after - set_items_before, '+'))
    diff_dic.update(_modify_keys(set_items_before - set_items_after, '-'))
    diff_dic.update(dict(set_items_before & set_items_after))

    return json.dumps(diff_dic)
