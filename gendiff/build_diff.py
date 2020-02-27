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
    common = {}
    common.update(
        {
            key: (ADDED, after_dict[key])
            for key in sorted(after_dict.keys() - before_dict.keys())
        },
    )
    common.update(
        {
            key: (DELETED, before_dict[key])
            for key in sorted(before_dict.keys() - after_dict.keys())
        },
    )
    for key in sorted(after_dict.keys() & before_dict.keys()):
        old_value = before_dict.get(key)
        new_value = after_dict.get(key)
        has_children = (
            isinstance(old_value, dict)
        ) and (
            isinstance(new_value, dict)
        )
        if has_children:
            common[key] = (
                NESTED,
                build_diff(old_value, new_value),
            )
        elif old_value == new_value:
            common[key] = (UNCHANGED, old_value)
        else:
            common[key] = (CHANGED, old_value, new_value)
    return common
