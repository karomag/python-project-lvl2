# -*- coding: utf-8 -*-

"""Render diff as json."""


from gendiff.constants import (
    ADDED,
    AFTER_VALUE,
    BEFORE_VALUE,
    CHANGED,
    CHILDREN,
    DELETED,
    INDENT,
    NESTED,
    TYPE_NODE,
    UNCHANGED,
    VALUE,
)


def render(diff: dict, level: int = 1):
    """Render diff to json.

    Args:
        diff: input diff
        level: nesting depth

    Returns:
        report string
    """
    report_list = []
    indent = INDENT * level

    for key, value_diff in diff.items():
        type_key = value_diff.get(TYPE_NODE)

        if type_key == NESTED:
            report_list.append('{0}{1} {2}: {{'.format(indent, UNCHANGED, key))
            report_list.append(render(value_diff.get(CHILDREN), level + 2))
            report_list.append('{0}}}'.format(indent + INDENT))
        elif type_key == CHANGED:
            report_list.append('{0}{1} {2}: {3}'.format(
                indent,
                DELETED,
                key,
                value_diff.get(BEFORE_VALUE),
            ),
            )
            report_list.append('{0}{1} {2}: {3}'.format(
                indent,
                ADDED,
                key,
                value_diff.get(AFTER_VALUE),
            ),
            )
        else:
            report_list.append('{0}{1} {2}: {3}'.format(
                indent,
                type_key,
                key,
                _value_to_string(value_diff.get(VALUE), level),
            ),
            )

    if level == 1:
        report_list = ['{'] + report_list + ['}']
    return '\n'.join(report_list)


def _value_to_string(input_value, level: int = 1):
    if isinstance(input_value, dict):
        lines = ['{']
        for key, value_dict in input_value.items():
            lines.append('{0}{1}: {2}'.format(
                INDENT * (level + 3),
                key,
                value_dict,
            ),
            )
            lines.append('{0}}}'.format(INDENT * (level + 1)))
        return '\n'.join(lines)
    if isinstance(input_value, bool):
        return str(input_value).lower()
    return input_value
