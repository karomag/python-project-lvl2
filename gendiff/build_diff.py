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


def _check_key(before_value, after_value):
    if before_value == after_value:
        type_tag = UNCHANGED
    else:
        type_tag = CHANGED
    if after_value is None:
        type_tag = DELETED
    if before_value is None:
        type_tag = ADDED

    node = {
        ADDED: {
            TYPE_NODE: ADDED,
            VALUE: after_value,
        },
        CHANGED: {
            TYPE_NODE: CHANGED,
            BEFORE_VALUE: before_value,
            AFTER_VALUE: after_value,
        },
        DELETED: {
            TYPE_NODE: DELETED,
            VALUE: before_value,
        },
        UNCHANGED: {
            TYPE_NODE: UNCHANGED,
            VALUE: before_value,
        },
    }
    return node[type_tag]


def _build_diff(before_value, after_value):
    have_children = (
        isinstance(before_value, dict)
    ) and (
        isinstance(after_value, dict)
    )
    if have_children:
        node = {key: _build_diff(before_value.get(key), after_value.get(key))
            for key in sorted(before_value.keys() | after_value.keys())
        }
        for key in sorted(before_value.keys() | after_value.keys()):
            node = {
                TYPE_NODE: NESTED,
                CHILDREN: _build_diff(
                    before_value.get(key),
                    after_value.get(key),
                ),
        }
    else:
        node = _check_key(before_value, after_value)
    return node


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

    diff = {key: _build_diff(before_dict.get(key), after_dict.get(key))
        for key in sorted(before_dict.keys() | after_dict.keys())
    }
    print(diff)
    return nested_render.render(diff)
