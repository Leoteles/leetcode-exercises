# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# 44% 36%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self,node):
        if node is None:
            return 0

        left = self.traverse(node.left)
        right = self.traverse(node.right)
        return max(left+1,right+1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root)