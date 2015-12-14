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


def in_order_traversal_iterative(root):
    res, stack = [], deque([])
    curr = root
    while len(stack) > 0 or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def pre_order_traversal_recursive(root):
    res = []
    if root is None:
        return res
    res.append(root.val)
    res += pre_order_traversal_recursive(root.left)
    res += pre_order_traversal_recursive(root.right)
    return res


def pre_order_traversal_iterative(root):
    res, stack = [], deque([])
    stack.append(root)
    while len(stack) > 0:
        tmp = stack.pop()
        res.append(tmp.val)
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)
    return res


def post_order_traversal_recursive(root):
    res = []
    if root is None:
        return res
    res += post_order_traversal_recursive(root.left)
    res += post_order_traversal_recursive(root.right)
    res.append(root.val)
    return res


def post_order_traversal_iterative(root):
    res, stack = [], deque([])
    curr, prev = root, None
    stack.append(curr)
    while len(stack) > 0:
        curr = stack[-1]
        if prev is None or prev.left == curr or prev.right == curr:
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
        elif curr.left == prev:
            if curr.right:
                stack.append(curr.right)
        else:
            stack.pop()
            res.append(curr.val)
        prev = curr
    return res


def main():
    my_bst = MyBinarySearchTree.BST()
    NUMS = [4, 2, 1, 3, 6, 5, 7]
    for i in NUMS:
        my_bst.insert(i)
    root_node = my_bst.root

    level_order = level_order_traversal(my_bst)
    print 'level order:', level_order

    in_order_recursive = in_order_traversal_recursive(root_node)
    print 'in order recursive:', in_order_recursive

    in_order_iterative = in_order_traversal_iterative(root_node)
    print 'in order iterative:', in_order_iterative

    pre_order_recursive = pre_order_traversal_recursive(root_node)
    print 'pre order recursive:', pre_order_recursive

    pre_order_iterative = pre_order_traversal_iterative(root_node)
    print 'pre order iterative:', pre_order_iterative

    post_order_recursive = post_order_traversal_recursive(root_node)
    print 'post order recursive:', post_order_recursive

    post_order_iterative = post_order_traversal_iterative(root_node)
    print 'post order iterative:', post_order_iterative

    my_bst.delete(2)
    level_order = level_order_traversal(my_bst)
    print 'level order:', level_order

    my_bst.delete(4)
    level_order = level_order_traversal(my_bst)
    print 'level order:', level_order


if __name__ == '__main__':
    main()
