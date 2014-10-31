class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    root = None

    def preorder_tree(self):
        return self.preorder(self.root)

    def preorder(self, node):
        if node is None:
            return
        else:
            yield node.data
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)
