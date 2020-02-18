# -*- coding: utf-8 -*-

"""Tests for generate_diff."""

import json

from gendiff.build_diff import build_diff, generate_diff, read_file


def test_generate_diff_nested_structures():
    """Test generate_diff for nested structures files."""
    result_generate_diff = generate_diff(
        'gendiff/tests/fixtures/before.json',
        'gendiff/tests/fixtures/after.json',
    )
    with open('gendiff/tests/fixtures/diff_nested_structures.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_generate_diff_yaml():
    """Test generate_diff for plane yml files."""
    result_generate_diff = generate_diff(
        'gendiff/tests/fixtures/before.yml',
        'gendiff/tests/fixtures/after.yml',
    )
    with open('gendiff/tests/fixtures/diff_plain_files.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_build_diff():
    """Test build diff."""
    before_dict = read_file('gendiff/tests/fixtures/before.json')
    after_dict = read_file('gendiff/tests/fixtures/after.json')
    with open('gendiff/tests/fixtures/build_diff.txt') as inf:
        correct_answer = inf.read()
    assert json.dumps(build_diff(before_dict, after_dict)) == correct_answer
