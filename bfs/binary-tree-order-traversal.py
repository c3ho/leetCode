# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check root
        if not root:
            return []

        # if not empty, initialize deques to hold values
        # we need three lists:
        # a. one to keep track of our progress
        # b. one to track the children we'll need to visit
        # c. one to track the output
        # a and b cannot be done at the same time, otherwise we'll lose track of which
        # node is the parent and which are the children node as they'll belong in different
        # lists
        stack = deque([root])
        output = [[root.val]]
        children = deque()

        # When the stack is empty, we'll have gone through all nodes
        while stack:
            # get curr node
            curr = stack.popleft()

            # append children nodes
            if curr.left:
                children.append(curr.left)
            if curr.right:
                children.append(curr.right)

            if not stack:
                # if there are children, we'll append the childrens' values to the output
                # using list comprehension. The queueing of the children nodes has already
                # been done in the above if statements
                if children:
                    output.append([c.val for c in children])
                # set the stack nodes as the children nodes to iterate through the next level
                stack.extend(children)
                # reset the children so we'll have a clean slate for the next level of nodes
                children = deque()

        return output
