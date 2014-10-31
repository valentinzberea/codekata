from unittest import TestCase
from .binary_tree import BinaryTree, TreeNode


class TestBinaryTree(TestCase):

    def test_traverse_empty_tree(self):
        tree = BinaryTree()
        self.assertEqual(list(tree.preorder_tree()), [])

    def test_traverse_tree(self):
        tree = BinaryTree()

        root = TreeNode(0)
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        root.left = n1
        root.right = n2

        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n1.left = n3
        n1.right = n4

        n5 = TreeNode(5)
        n6 = TreeNode(6)
        n2.left = n5
        n2.right = n6

        tree.root = root
        self.assertEqual(list(tree.preorder_tree()),
                          [0, 1, 3, 4, 2, 5, 6])
