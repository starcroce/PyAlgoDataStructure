class AVLNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

    def balance_factor(self):
        if self.left is None and self.right is None:
            return 0
        if self.left is None:
            return 0 - self.right.height - 1
        if self.right is None:
            return self.left.right + 1
        return self.left.height - self.right.height


class AVLTree:

    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def single_right_rotation(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        tmp.height = max(self.get_height(node), self.get_height(tmp.left)) + 1
        return tmp

    def single_left_rotation(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        tmp.height = max(self.get_height(node), self.get_height(tmp.right)) + 1
        return tmp

    def double_right_rotation(self, node):
        node.left = self.single_left_rotation(node.left)
        return self.single_right_rotation(node)

    def double_left_rotation(self, node):
        node.right = self.single_right_rotation(node.right)
        return self.single_left_rotation(node)

    def avl_insert(self, node, val):
        if node is None:
            node = AVLNode(val)
        elif node.val < val:
            node.right = self.avl_insert(node.right, val)
            if node.balance_factor() == -2:
                if node.right.balance_factor() == -1:
                    node = self.single_left_rotation(node)
                elif node.right.balance_factor() == 1:
                    node = self.double_left_rotation(node)
        else:
            node.left = self.avl_insert(node.left, val)
            if node.balance_factor() == 2:
                if node.left.balance_factor() == 1:
                    node = self.single_right_rotation(node)
                elif node.left.balance_factor() == -1:
                    node = self.double_right_rotation(node)
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return node

    def avl_search(self, node, val):
        if node is None:
            return None
        if node.val > val:
            return self.avl_search(node.left, val)
        elif node.val < val:
            return self.avl_search(node.right, val)
        elif node.val == val:
            return node

