from unittest import TestCase
from .insertion_sort import InsertionSort


class TestInsertionSort(TestCase):

    def test_sort(self):
        strategy = InsertionSort()
        sorted_array = strategy.sort([2, 1])
        self.assertEqual(sorted_array, [1, 2])
