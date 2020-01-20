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
    before_file = read_file(path_to_file_before)
    after_file = read_file(path_to_file_after)
    # diff_dic = dict(modify_keys(set_items_before & set_items_after))
    # diff_dic.update(modify_keys(set_items_after - set_items_before, '+'))
    # diff_dic.update(modify_keys(set_items_before - set_items_after, '-'))

    # diff_string = '{\n'
    # for key_dic in sorted(diff_dic.keys(), key=lambda element: element[2:]):
    #    diff_string += ' {0}: {1}\n'.format(key_dic, diff_dic[key_dic])
    # diff_string += '}'

    return before_file.keys()
