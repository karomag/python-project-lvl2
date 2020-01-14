# -*- coding: utf-8 -*-

"""Generate diff."""

import json
from os import path

import yaml


def _get_set_from_json(path_to_file):
    with open(path.abspath(path_to_file)) as inf:
        return set(json.load(inf).items())


def _get_set_from_yaml(path_to_file):
    with open(path.abspath(path_to_file)) as inf:
        return set(yaml.safe_load(inf).items())


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
        str; diff string
    """
    if path.splitext(path.basename(path_to_file_before)) == '.json':
        set_items_before = _get_set_from_json(path_to_file_before)
        set_items_after = _get_set_from_json(path_to_file_after)
    else:
        set_items_before = _get_set_from_yaml(path_to_file_before)
        set_items_after = _get_set_from_yaml(path_to_file_after)
    diff_dic = dict(_modify_keys(set_items_before & set_items_after))
    diff_dic.update(_modify_keys(set_items_after - set_items_before, '+'))
    diff_dic.update(_modify_keys(set_items_before - set_items_after, '-'))

    diff_string = '{\n'
    for key_dic in sorted(diff_dic.keys(), key=lambda element: element[2:]):
        diff_string += ' {0}: {1}\n'.format(key_dic, diff_dic[key_dic])
    diff_string += '}'

    return diff_string
