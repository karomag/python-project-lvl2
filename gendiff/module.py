# -*- coding: utf-8 -*-

"""Generate diff."""

import json
from os import path

import yaml


def get_set_from_file(path_to_file):
    """Get set from file.

    Args:
        path_to_file: file to loading

    Returns:
        set
    """
    with open(path.abspath(path_to_file)) as inf:
        if path.splitext(path.basename(path_to_file)) == '.json':
            return set(json.load(inf).items())
        return set(yaml.safe_load(inf).items())


def modify_keys(input_set, symbol=' '):
    """Modify set to dictionary adding symbol to key.

    Args:
        input_set: set
        symbol: str

    Returns:
        dict
    """
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
        str; diff string
    """
    set_items_before = get_set_from_file(path_to_file_before)
    set_items_after = get_set_from_file(path_to_file_after)
    diff_dic = dict(modify_keys(set_items_before & set_items_after))
    diff_dic.update(modify_keys(set_items_after - set_items_before, '+'))
    diff_dic.update(modify_keys(set_items_before - set_items_after, '-'))

    diff_string = '{\n'
    for key_dic in sorted(diff_dic.keys(), key=lambda element: element[2:]):
        diff_string += ' {0}: {1}\n'.format(key_dic, diff_dic[key_dic])
    diff_string += '}'

    return diff_string
