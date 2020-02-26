# -*- coding: utf-8 -*-

"""Render diff like nested."""


from gendiff.constants import (
    ADDED,
    CHANGED,
    DELETED,
    INDENT,
    NESTED,
    UNCHANGED,
)

operators = {
    ADDED: '+',
    DELETED: '-',
    UNCHANGED: ' ',
}


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

    for key, (type_key, *option_value) in diff.items():  # noqa: WPS405, WPS414
        def inner_append(operator, inner_value):  # noqa: WPS430
            report_list.append('{0}{1} {2}: {3}'.format(
                indent,
                operators[operator],
                key,
                inner_value,
            ),
            )

        if type_key == NESTED:
            inner_append(UNCHANGED, '{')
            report_list.append(render(option_value[0], level + 2))
            report_list.append('{0}}}'.format(indent + INDENT))
        elif type_key == CHANGED:
            inner_append(DELETED, _value_to_string(option_value[0]))
            inner_append(ADDED, _value_to_string(option_value[1]))
        else:
            inner_append(type_key, _value_to_string(option_value[0], level))

    if level == 1:
        report_list = ['{'] + report_list + ['}']
    return '\n'.join(report_list)


def _value_to_string(input_value, level=1):
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
