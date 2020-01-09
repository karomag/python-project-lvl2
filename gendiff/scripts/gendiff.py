#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Gendiff main script."""

import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.parse_args()


def main():
    """Starting point."""
    print('pass')


if __name__ == '__main__':
    main()
