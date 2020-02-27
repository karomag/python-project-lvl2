#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff main script."""

from gendiff.build_diff import generate_diff
from gendiff.parser import parse_args, read_file


def main():
    """Run cli."""
    options = parse_args()
    diff_string = generate_diff(
        read_file(options.first_file),
        read_file(options.second_file),
        options.format,
    )
    print(diff_string)


if __name__ == '__main__':
    main()
