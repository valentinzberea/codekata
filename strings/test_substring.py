from unittest import TestCase
from .substring import substring


class TestSubstring(TestCase):

    def test_substring(self):
        self.assertEqual(substring('', ''), -1)
        self.assertEqual(substring('aab', 'b'), 2)
        self.assertEqual(substring('a', 'bb'), -1)
        self.assertEqual(substring('a', 'a'), 0)
        self.assertEqual(substring('abbccdd', 'ccd'), 3)
        self.assertEqual(substring('abbccdd', 'abb'), 0)
        self.assertEqual(substring('abbccdd', 'abbccdd'), 0)
