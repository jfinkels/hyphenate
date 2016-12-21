# test_hyphenate.py - unit tests for Hyphenate
#
# This file is part of Hyphenate. The authors of Hyphenate abandon all
# claims to copyright, and dedicate it to the public domain.
"""Unit tests for hyphenating words."""
from unittest import TestCase

from hyphenate import hyphenate_word


class TestHyphenation(TestCase):

    def test_short_word(self):
        computed = hyphenate_word('the')
        expected = ['the']
        self.assertEqual(computed, expected)

    def test_medium_word(self):
        computed = hyphenate_word('hyphenation')
        expected = ['hy', 'phen', 'ation']
        self.assertEqual(computed, expected)

    def test_long_word(self):
        computed = hyphenate_word('supercalifragilisticexpialidocious')
        expected = ['su', 'per', 'cal', 'ifrag', 'ilis', 'tic', 'ex', 'pi',
                    'ali', 'do', 'cious']
        self.assertEqual(computed, expected)

    def test_exception_word(self):
        computed = hyphenate_word('associate')
        expected = ['as', 'so', 'ciate']
        self.assertEqual(computed, expected)
