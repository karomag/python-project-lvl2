# -*- coding: utf-8 -*-

"""Tests for generate_diff."""

import json

from gendiff import format
from gendiff.build_diff import build_diff, generate_diff
from gendiff.parser import read_file

PATH_AFTER = 'tests/fixtures/after.json'
PATH_BEFORE = 'tests/fixtures/before.json'


def _get_result_gendiff(formater):
    return generate_diff(
        read_file(PATH_BEFORE),
        read_file(PATH_AFTER),
        formater,
    )


def test_generate_diff():
    """Test generate_diff."""
    with open('tests/fixtures/formatter_plain.txt') as inf_plain:
        correct_answer = inf_plain.read()
    assert _get_result_gendiff(format.plain) == correct_answer

    with open('tests/fixtures/formatter_nested.txt') as inf_nested:
        correct_answer = inf_nested.read()
    assert _get_result_gendiff(format.nested) == correct_answer

    with open('tests/fixtures/formatter_json.txt') as inf_json:
        correct_answer = inf_json.read()
    assert _get_result_gendiff(format.json) == correct_answer


def test_build_diff():
    """Test build diff."""
    before_dict = read_file(PATH_BEFORE)
    after_dict = read_file(PATH_AFTER)
    with open('tests/fixtures/build_diff.txt') as inf:
        correct_answer = inf.read()
    assert json.dumps(build_diff(before_dict, after_dict)) == correct_answer
