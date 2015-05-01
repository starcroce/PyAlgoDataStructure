import MyBinarySearchTree


my_bst = MyBinarySearchTree.BST()
print my_bst.insert(0)
print my_bst.insert(-1)
print my_bst.insert(1)
print my_bst.insert(0)

print my_bst.root.val, my_bst.root.left.val, my_bst.root.right.val

print my_bst.find(0)
print my_bst.find(-1)
print my_bst.find(1)
print my_bst.find(2)