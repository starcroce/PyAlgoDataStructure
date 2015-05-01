class BSTNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, val):
        new_tree_node = BSTNode(val)
        if self.root is None:
            self.root = new_tree_node
            return True
        curr = self.root
        while curr:
            if val < curr.val:
                if curr.left is None:
                    curr.left = new_tree_node
                    return True
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = new_tree_node
                    return True
                curr = curr.right
            else:
                return False
        return False

    def find(self, val):
        res = self.root
        while res:
            if val == res.val:
                return True
            elif val > res.val:
                res = res.right
            elif val < res.val:
                res = res.left
        return False
