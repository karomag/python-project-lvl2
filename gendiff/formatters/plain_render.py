# -*- coding: utf-8 -*-

"""Render diff as plain."""

from gendiff.constants import ADDED, CHANGED, DELETED, NESTED, UNCHANGED

strings = {
    ADDED: "Property '{0}' was added with value: '{1}'",
    DELETED: "Property '{0}' was removed",
    CHANGED: "Property '{0}' was changed. From '{1}' to '{2}'",
}


def render(diff: dict, keys: list = None):
    """Render diff like plain.

    Args:
        diff: input diff
        keys: if key has children

    Returns:
        report string
    """
    report_list = []

    if keys is None:
        keys = []

    for key in diff.keys():
        type_key, *value_key = diff[key]
        if type_key == UNCHANGED:
            continue

        if type_key == NESTED:
            keys.append(key)
            report_list.append(render(value_key[0], keys))
        elif type_key == CHANGED:
            keys.append(key)
            report_list.append(
                strings[CHANGED].format(
                    '.'.join(keys),
                    _value_to_string(value_key[0]),
                    _value_to_string(value_key[1]),
                ),
            )
            keys.pop()
        elif type_key == ADDED:
            keys.append(key)
            report_list.append(
                strings[ADDED].format(
                    '.'.join(keys),
                    _value_to_string(value_key[0]),
                ),
            )
            keys.pop()
        elif type_key == DELETED:
            keys.append(key)
            report_list.append(strings[DELETED].format('.'.join(keys)))
            keys.pop()

    keys.clear()

    return '\n'.join(report_list)


def _value_to_string(input_value):
    if isinstance(input_value, dict):
        return 'complex value'
    if isinstance(input_value, bool):
        return str(input_value).lower()
    return str(input_value)
