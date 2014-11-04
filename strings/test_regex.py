from unittest import TestCase
from .regex import Regex


class TestInsertionSort(TestCase):

    def test_regex_on_empty_string(self):
        self.assertEqual(Regex().match('', ''), [])

    def test_regex_on_string(self):
        self.assertEqual(Regex().match('', 'aa-11, bb-22'),
                         [])
        self.assertEqual(Regex().match('-.', 'aa-11, bb-22'),
                         ['-1', '-2'])
        self.assertEqual(Regex().match('-.*', 'aa-11, bb-22'),
                         ['-11, bb-22'])
        self.assertEqual(Regex().match('.*-.*', 'aa-11, bb-22'),
                         ['aa-11, bb-22'])
