class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self, root_key):
        self.root = TreeNode(root_key)

    def insert(self, key):
        self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

# Пример использования бинарного дерева
tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.inorder_traversal(tree.root)  # Вывод: 2 5 7 10 15
