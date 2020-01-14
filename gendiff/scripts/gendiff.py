#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff main script."""

from gendiff.module import generate_diff
from gendiff.parsers import parse_args


def main():
    """Run cli."""
    options = parse_args()
    diff_string = generate_diff(options.first_file, options.second_file)
    print(diff_string)


if __name__ == '__main__':
    main()
