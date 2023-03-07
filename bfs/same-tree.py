# https://leetcode.com/problems/same-tree/

###
# Leetcode question 100
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
###


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Pretty simple, just checking if the left tree is equivalent to the right tree with node placements in the same spots
# Approach - check root node of p and q, if values are the same check left and right

# O(n) time, because we have to check every node
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both nodes are null so they're fine
        if not p and not q:
            return True
        # one of the nodes are empty while the other one isn't means trees are not equivalent
        if not p or not q:
            return False
        # if the root node is same value check the children nodes
        if (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
