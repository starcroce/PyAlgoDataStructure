from collections import deque

import MyBinarySearchTree


def level_order_traverse(bst):
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


def main():
    my_bst = MyBinarySearchTree.BST()
    NUMS = [4, 2, 1, 3, 6, 5, 7]
    for i in NUMS:
        my_bst.insert(i)

    level_order = level_order_traverse(my_bst)
    print level_order


if __name__ == '__main__':
    main()
