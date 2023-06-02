#%%
# https://leetcode.com/problems/balanced-binary-tree/
# solution counting the nodes
#Returns 0 if there is no node, 1 for one level, 2 for 2 levels, etc

class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            #left == -1 or right == -1 propagates 
            # the unbalanced result to the caller
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1

# 226 / 226 test cases passed.
# Status: Accepted
# Runtime: 80 ms

#%%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverse(root) != -1
    def traverse(self,root,depth = 1):
        if not root and depth == 1:
            return True
        elif not root:
            return depth - 1
        left = self.traverse(root.left,depth+1)
        if left == -1:
            return -1
        right = self.traverse(root.right,depth+1)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left,right)


#%%%
