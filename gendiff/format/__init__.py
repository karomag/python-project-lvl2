# -*- coding: utf-8 -*-

"""Renders."""

from gendiff.format.json import render as json
from gendiff.format.nested import render as nested
from gendiff.format.plain import render as plain

__all__ = ['json', 'nested', 'plain']
