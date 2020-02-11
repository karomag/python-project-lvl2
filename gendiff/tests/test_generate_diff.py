# -*- coding: utf-8 -*-

"""Tests for generate_diff."""

from gendiff.build_diff import generate_diff


def test_generate_diff_json():
    """Test generate_diff for plane json files."""
    result_generate_diff = generate_diff(
        'gendiff/tests/fixtures/before.json',
        'gendiff/tests/fixtures/after.json',
    )
    with open('gendiff/tests/fixtures/diff_nested_structures.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer
