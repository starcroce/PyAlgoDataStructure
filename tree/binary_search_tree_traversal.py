from collections import deque

import MyBinarySearchTree


def level_order_traversal(bst):
    res, level, root = [], [], bst.root
    queue = deque([root, None])
    while len(queue) > 0:
        tmp = queue.popleft()
        if tmp:
            level.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        else:
            res.append(level)
            level = []
            if len(queue) > 0:
                queue.append(None)
    return res


def in_order_traversal_recursive(root):
    res = []
    if root is None:
        return res
    res += in_order_traversal_recursive(root.left)
    res.append(root.val)
    res += in_order_traversal_recursive(root.right)
    return res


def pre_order_traversal_recursive(root):
    res = []
    if root is None:
        return res
    res.append(root.val)
    res += pre_order_traversal_recursive(root.left)
    res += pre_order_traversal_recursive(root.right)
    return res


def post_order_traversal_recursive(root):
    res = []
    if root is None:
        return res
    res += post_order_traversal_recursive(root.left)
    res += post_order_traversal_recursive(root.right)
    res.append(root.val)
    return res


def main():
    my_bst = MyBinarySearchTree.BST()
    NUMS = [4, 2, 1, 3, 6, 5, 7]
    for i in NUMS:
        my_bst.insert(i)

    level_order = level_order_traversal(my_bst)
    print level_order

    in_order_recursive = in_order_traversal_recursive(my_bst.root)
    print in_order_recursive
    
    pre_order_recursive = pre_order_traversal_recursive(my_bst.root)
    print pre_order_recursive

    post_order_recursive = post_order_traversal_recursive(my_bst.root)
    print post_order_recursive


if __name__ == '__main__':
    main()
