# -*- coding: utf-8 -*-

"""Render diff as json."""

import json


def render(diff: dict):
    """Render diff like json.

    Args:
        diff: input diff

    Returns:
        report string
    """
    return json.dumps(diff, indent=2)
