# -*- coding: utf-8 -*-

"""Generate diff."""

from gendiff.constants import ADDED, CHANGED, DELETED, NESTED, UNCHANGED


def generate_diff(
    before_dict: dict,
    after_dict: dict,
    output_format,
):
    """Find differences in files.

    Args:
        before_dict: first dictionary from file
        after_dict: secondary dictionary from file
        output_format: format.plain(), format.nested(), format.json()

    Returns:
        str: diff string
    """
    diff = build_diff(before_dict, after_dict)
    return output_format(diff)


def build_diff(before_dict: dict, after_dict: dict):
    """Build structure report.

    Args:
        before_dict: before dataset
        after_dict: after dataset

    Returns:
        diff (dict)
    """
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
                build_diff(before_dict.get(key), after_dict.get(key)),
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
