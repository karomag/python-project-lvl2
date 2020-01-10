# -*- coding: utf-8 -*-

"""Generate diff."""

import argparse
import json
import sys


def parse_args():
    """Parse arguments.

    Automatically generate help and usage messages.

    Returns:
        option: Inspect the command line, convert each argument
                to the appropriate type.
    """
    parser = argparse.ArgumentParser(
        description=sys.modules[__name__].__doc__,
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    group = parser.add_argument_group('format settings')
    group.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def generate_diff(path_to_file1, path_to_file2):
    """Find differences in files.

    Args:
        path_to_file1: path to file1
        path_to_file2: path to file2

    Returns:
        file1, file2
    """
    with open(path_to_file1) as inf1:
        file1 = json.load(inf1)
    with open(path_to_file2) as inf2:
        file2 = json.load(inf2)

    return file1, file2
