# -*- coding: utf-8 -*-

"""Tests for generate_diff."""

import json

from gendiff.build_diff import build_diff, generate_diff, read_file

PATH_AFTER = 'gendiff/tests/fixtures/after.json'

PATH_BEFORE = 'gendiff/tests/fixtures/before.json'


def test_generate_diff_plain_format():
    """Test generate_diff the plain format."""
    result_generate_diff = generate_diff(
        PATH_BEFORE,
        PATH_AFTER,
    )
    with open('gendiff/tests/fixtures/formatter_plain.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_generate_diff_nested_format():
    """Test generate_diff the nested format."""
    result_generate_diff = generate_diff(
        PATH_BEFORE,
        PATH_AFTER,
        'nested',
    )
    with open('gendiff/tests/fixtures/formatter_nested.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_generate_diff_nested_json():
    """Test generate_diff the json format."""
    result_generate_diff = generate_diff(
        PATH_BEFORE,
        PATH_AFTER,
        'json',
    )
    with open('gendiff/tests/fixtures/formatter_json.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_generate_diff_yaml():
    """Test generate_diff for plane yml files."""
    result_generate_diff = generate_diff(
        'gendiff/tests/fixtures/before.yml',
        'gendiff/tests/fixtures/after.yml',
        'nested',
    )
    with open('gendiff/tests/fixtures/diff_plain_files.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_build_diff():
    """Test build diff."""
    before_dict = read_file(PATH_BEFORE)
    after_dict = read_file(PATH_AFTER)
    with open('gendiff/tests/fixtures/build_diff.txt') as inf:
        correct_answer = inf.read()
    assert json.dumps(build_diff(before_dict, after_dict)) == correct_answer
