# -*- coding: utf-8 -*-

"""The option parser."""

import argparse
import json
from os import path

import yaml

from gendiff import format


def _parse_file(inf, file_format):
    parser = {
        '.json': json.loads,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load,
    }
    return parser[file_format](inf)


def read_file(path_to_file: str):
    """Get dictionary from file.

    Args:
        path_to_file: path to file

    Returns:
        formatted data
    """
    with open(path.abspath(path_to_file)) as inf:
        return _parse_file(
            inf.read(),
            path.splitext(path.basename(path_to_file))[1],
        )


def formatters(format_string: str = 'plain'):
    """Get parser's function to format.

    Args:
        format_string: formatting option

    Returns:
        function of parse
    """
    formatter = {
        'plain': format.plain,
        'nested': format.nested,
        'json': format.json,
    }
    return formatter[format_string]


def parse_args():
    """Parse arguments.

    Automatically generate help and usage messages.

    Returns:
        option: Inspect the command line, convert each argument
                to the appropriate type.
    """
    parser = argparse.ArgumentParser(
        description='Generate diff.',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    group = parser.add_argument_group('format settings')
    group.add_argument(
        '-f',
        '--format',
        type=formatters,
        default='plain',
        help='set format of output (default: plain)',
    )

    return parser.parse_args()
