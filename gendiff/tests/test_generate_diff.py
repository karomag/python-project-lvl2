# -*- coding: utf-8 -*-

"""Tests for generate_diff."""

from gendiff.module import generate_diff, modify_keys


def test_generate_diff_json():
    """Test generate_diff for plane json files."""
    result_generate_diff = generate_diff(
        'gendiff/tests/fixtures/before.json',
        'gendiff/tests/fixtures/after.json',
    )
    with open('gendiff/tests/fixtures/diff_nested_structures.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_generate_diff_yaml():
    """Test generate_diff for yaml files."""
    result_generate_diff = generate_diff(
        'gendiff/tests/fixtures/before.yml',
        'gendiff/tests/fixtures/after.yml',
    )
    with open('gendiff/tests/fixtures/diff_before_after.txt') as inf:
        correct_answer = inf.read()
    assert result_generate_diff == correct_answer


def test_modify_keys():
    """Test modify keys."""
    dic = modify_keys({('key1', 'value1'), ('key2', 'value2')}, '+')
    assert dic == {'+ key1': 'value1', '+ key2': 'value2'}
