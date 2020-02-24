#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff main script."""

import argparse

from gendiff import format
from gendiff.build_diff import generate_diff


def _formatters(format_string='plain'):
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
        type=_formatters,
        default='plain',
        help='set format of output (default: plain)',
    )

    return parser.parse_args()


def main():
    """Run cli."""
    options = parse_args()
    diff_string = generate_diff(
        options.first_file,
        options.second_file,
        options.format,
    )
    print(diff_string)


if __name__ == '__main__':
    main()
