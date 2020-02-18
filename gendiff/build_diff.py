# -*- coding: utf-8 -*-

"""Generate diff."""

import json
from os import path

import yaml

from gendiff.constants import (
    ADDED,
    AFTER_VALUE,
    BEFORE_VALUE,
    CHANGED,
    CHILDREN,
    DELETED,
    NESTED,
    TYPE_NODE,
    UNCHANGED,
    VALUE,
)
from gendiff.formatters import nested_render


def generate_diff(path_to_file_before, path_to_file_after):
    """Find differences in files.

    Args:
        path_to_file_before: path to file1
        path_to_file_after: path to file2

    Returns:
        str; diff string
    """
    before_dict = _read_file(path_to_file_before)
    after_dict = _read_file(path_to_file_after)

    diff = _build_diff(before_dict, after_dict)
    print(diff)
    return nested_render.render(diff)


def _build_diff(before_dict, after_dict):
    nodes = {}
    for key in sorted(before_dict.keys() | after_dict.keys()):
        have_children = (
            isinstance(before_dict.get(key), dict)
        ) and (
            isinstance(after_dict.get(key), dict)
        )
        if have_children:
            nodes[key] = (
                NESTED,
                _build_diff(before_dict.get(key), after_dict.get(key)),
            )
        else:
            nodes[key] = _check_key(key, before_dict, after_dict)
    return nodes


def _check_key(key, before_dict, after_dict):
    set1 = set(before_dict.keys())
    set2 = set(after_dict.keys())

    if key in set2 & set1:
        if before_dict.get(key) == after_dict.get(key):
            type_tag = UNCHANGED
        else:
            type_tag = CHANGED
    if key in set1 - set2:
        type_tag = DELETED
    if key in set2 - set1:
        type_tag = ADDED

    node = {
        ADDED: (ADDED, after_dict.get(key)),
        CHANGED: (CHANGED, before_dict.get(key), after_dict.get(key)),
        DELETED: (DELETED, before_dict.get(key)),
        UNCHANGED: (UNCHANGED, before_dict.get(key)),
    }
    return node[type_tag]


def _parse_file(inf, file_format):
    parser = {
        '.json': json.loads,
        '.yml': yaml.safe_load,
    }
    return parser[file_format](inf)


def _read_file(path_to_file):
    with open(path.abspath(path_to_file)) as inf:
        return _parse_file(
            inf.read(),
            path.splitext(path.basename(path_to_file))[1],
        )
