# Tree
"""
Characteristic
# Root          (Most top Node)
# Node          (Data Sets)
# Edge          (branch)
# Parent        (Node contains nodes)
# Child         (Nodes under node)
# Siblings Node (Nodes that under the same parent and in same layer)
# Leaf          (Bottom nodej)
# Subtree       (Tree under ones node)
# Ancestor      (Nodes that above ones node)
# Descendants   (Every nodes below ones node)

Binary Tree
# Each node can have up to 2 child nodes
"""

# Binary Search Tree
"""
Binary Search Tree(BST) Operations
# Insert
    # Start at root
    # Always insert as a leaf
    # less than root? -> put to left
    # larger than root? -> put to right
    # so on!
# Find
    # Start at root
    # less than root? -> search left
    # larger than root? -> search rightj
    # so on!
# Delete
    # 3 possible cases:
        # leaf node
            # just delete the leaf node
        # 1 child
            # promote the child to the target node's position (move to parent position)
        # 2 children
            # Find the next higher node
            # Always get higher
# get_size - counts all the node in the tree
    # return number of nodes. Works rescursively
    # size 1 += size(left) + size(right)
# traversals - walk through the tree node by node
    # Preorder Traversal
        # target
        # left
        # right
    # Inorder Traversal
        # left
        # target
        # right
    # Postorder Traversal
        # left
        # right
        # target
# Insert, Delete, Find in
O(h) = O(log n)
big o of the height of the tree
"""

import random


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert(self, data):
        if self.data == data:
            return False # duplicate value
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True
    def find(self, data):
        if self.data == data:
           return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data > data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
    def get_size(self):
        if self is None:
            return 0
        elif self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1
    def preorder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()
    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder()
    def postorder(self):
        if self is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data, end=' ')

tree = Tree(7)
tree.insert(9)

odd_list = [x for x in range(20) if x % 2 == 1]
random.shuffle(odd_list)
for i in odd_list:
    print(i, end=' ')
    tree.insert(i)
print()
tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
print()
print(tree.get_size())
