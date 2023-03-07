# https://leetcode.com/problems/symmetric-tree/
# 101. Given the root of a binary tree, check whether it is a mirror of itself(i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach - go with recursive, the root node will always be the same, but we'll have to check whether the left child's left node value
# is equal to the right child's right node value and left child's right node value is equal to the right child's left node value
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.isMirror(self, root.left, root.right)

    def isMirror(self, left, right) -> bool:
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        if left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
