#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff main script."""

from gendiff.cli import parse_args


def main():
    """Run cli."""
    options = parse_args()
    print(options)


if __name__ == '__main__':
    main()
