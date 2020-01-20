# -*- coding: utf-8 -*-

"""Parsers."""

import argparse
import json

import yaml


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
    group.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def parse_file(inf, file_format):
    """Read file and return dictionary.

    Args:
        inf: input file
        file_format: file extension

    Returns:
        dictionary
    """
    print(inf)
    print(file_format)
    parser = {
        '.json': json.loads,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load,
    }

    return parser[file_format](inf)
