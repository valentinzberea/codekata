from unittest import TestCase
from .linked_list import LinkedList


class TestLinkedList(TestCase):

    def test_create_empty_list(self):
        test_list = LinkedList()
        self.assertEqual(test_list.get_head(), None)

    def test_create_simple_list(self):
        test_list = LinkedList([1])
        self.assertEqual(test_list.get_head().data, 1)

    def test_print_values(self):
        test_list = LinkedList([3, 2, 1, 2])
        self.assertEqual(test_list.print_values(), '3,2,1,2')
