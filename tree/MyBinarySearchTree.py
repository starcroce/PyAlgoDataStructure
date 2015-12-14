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

    def delete(self, val):
        parent, curr = None, self.root
        while curr:
            if curr.val < val:
                parent = curr
                curr = curr.right
            elif curr.val > val:
                parent = curr
                curr = curr.left
            else:
                if curr.left is None and curr.right is None:
                    if curr == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                    return True
                elif curr.left is None:
                    if curr == parent.left:
                        parent.left = curr.right
                    else:
                        parent.right = curr.right
                    return True
                elif curr.right is None:
                    if curr == parent.left:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left
                    return True
                else:
                    target = self.find_successor(curr)
                    self.delete(target.val)
                    curr.val = target.val
                    return True
        return False

    def find_successor(self, node):
        if node.right:
            res = node.right
            while res.left:
                res = res.left
            return res
        res, curr = None, self.root
        while curr:
            if curr.val < node.val:
                curr = curr.right
            elif curr.val > node.val:
                res = curr
                curr = curr.left
            else:
                return res
