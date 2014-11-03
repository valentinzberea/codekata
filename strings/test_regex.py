from unittest import TestCase
from .regex import Regex


class TestInsertionSort(TestCase):

    def test_regex_on_empty_string(self):
        regex = Regex('.*-.?')
        self.assertEqual(regex.match(''), [])

    def test_regex_on_string(self):
        regex = Regex('.*-.?')
        self.assertEqual(regex.match('aa-11, bb-22'), ['aa-1', 'bb-2'])
