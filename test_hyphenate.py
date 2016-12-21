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
