# -*- coding: utf-8 -*-

"""Tests for generate_diff."""

from gendiff.module import generate_diff, get_set_from_file, modify_keys


def test_generate_diff_json():
    """Test generate_diff for plane json files."""
    result_generate_diff = generate_diff(
        'gendiff/tests/fixtures/before.json',
        'gendiff/tests/fixtures/after.json',
    )
    with open('gendiff/tests/fixtures/diff_before_after.txt') as inf:
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


def test_get_set_from_file():
    """Test get set from file."""
    dic = get_set_from_file('gendiff/tests/fixtures/before.json')
    assert dic == {
        ('host', 'hexlet.io'),
        ('timeout', 50),
        ('proxy', '123.234.53.22'),
        ('language', 'en'),
    }
