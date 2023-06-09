#%%
#https://leetcode.com/problems/validate-binary-search-tree/

#Solution 19% 41%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root,min_left = -float('inf'),max_right = float('inf')):
        if not root:
            return False
        
        if root.left:
            if root.left.val >= root.val:
                return False
            elif root.left.val <= min_left:
                return False
            else:
                left = self.isValidBST(root.left,min_left=min_left,max_right=root.val)
                if not left:
                    return False
        
        if root.right:
            if root.right.val <= root.val:
                return False
            elif root.right.val >= max_right:
                return False
            else:
                right = self.isValidBST(root.right,min_left=root.val,max_right=max_right)
                if not right:
                    return False
        
        return True
        