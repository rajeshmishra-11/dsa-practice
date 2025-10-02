#User function Template for python3
import sys
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.

def construct_from_pre(pre, idx, min_val, max_val):
    if idx[0] >= len(pre):
        return None

    key = pre[idx[0]]

    # If key is out of allowed range, skip
    if key <= min_val or key >= max_val:
        return None

    root = Node(key)
    idx[0] += 1  # move to next element

    # Build left and right subtrees
    root.left = construct_from_pre(pre, idx, min_val, key)
    root.right = construct_from_pre(pre, idx, key, max_val)

    return root

def Bst(pre, n):
    idx = [0]  # start from first element
    return construct_from_pre(pre, idx, -sys.maxsize, sys.maxsize)

# Preorder traversal to check result
def preorder(root, res):
    if not root:
        return
    res.append(root.data)
    preorder(root.left, res)
    preorder(root.right, res)