#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff main script."""

from gendiff.cli import generate_diff, parse_args


def main():
    """Run cli."""
    options = parse_args()
    res = generate_diff(options.first_file, options.second_file)
    print(res)


if __name__ == '__main__':
    main()
