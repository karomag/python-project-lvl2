# -*- coding: utf-8 -*-

"""Render diff as plain."""

from gendiff.constants import ADDED, CHANGED, DELETED, NESTED, UNCHANGED


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

        _string_report(type_key, key, value_key, report_list, keys)

    keys.clear()

    return '\n'.join(report_list)


def _add_added_node(key, value_key, report_list, keys):
    keys.append(key)
    report_list.append(
        "Property '{0}' was added with value: '{1}'".format(
            '.'.join(keys),
            _value_to_string(value_key[0]),
        ),
    )
    keys.pop()


def _add_deleted_node(key, report_list, keys):
    keys.append(key)
    report_list.append("Property '{0}' was removed".format('.'.join(keys)))
    keys.pop()


def _add_change_node(key, value_key, report_list, keys):
    keys.append(key)
    report_list.append(
        "Property '{0}' was changed. From '{1}' to '{2}'".format(
            '.'.join(keys),
            _value_to_string(value_key[0]),
            _value_to_string(value_key[1]),
        ),
    )
    keys.pop()


def _add_nested_node(key, value_key, report_list, keys):
    keys.append(key)
    report_list.append(render(value_key[0], keys))


def _string_report(type_key, key, value_key, report_list, keys):
    func = {
        ADDED: _add_added_node,
        CHANGED: _add_change_node,
        DELETED: _add_deleted_node,
        NESTED: _add_nested_node,
    }

    if type_key == DELETED:
        func[type_key](key, report_list, keys)
    else:
        func[type_key](key, value_key, report_list, keys)


def _value_to_string(input_value):
    if isinstance(input_value, dict):
        return 'complex value'
    if isinstance(input_value, bool):
        return str(input_value).lower()
    return str(input_value)
