#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_neotheicebird
----------------------------------

Tests for `neotheicebird` module.
"""

import pytest
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def test_if_import_prints_aboutme():
    with Capturing() as screen_out:
        import neotheicebird

    assert isinstance(screen_out, list)
    assert len(screen_out) > 0
    assert all(isinstance(line, str) for line in screen_out)
