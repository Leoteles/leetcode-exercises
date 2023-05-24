# https://leetcode.com/problems/diameter-of-binary-tree/

#%%
# leetcode

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
            
        depth(root)
        return self.ans


#%%
# 61% 46%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _,max_diam = self.len_diam_tree(root)
        return max_diam
    
    def len_diam_tree(self,root):
        if root is None:
            return 0,0
        
        len_left,diam_left = self.len_diam_tree(root.left)
        len_right,diam_right = self.len_diam_tree(root.right)
        
        #1+max(len_left,len_right) is the maximum length between left and right nodes
        return 1+max(len_left,len_right),max(diam_left,diam_right,len_left+len_right)

# 2l - 1,0
# 2r - 1,0
# 1l - 2,1+1=2 => 2,2
# 1r - 1,0
# resp = 3,max(2,0,2+1)




#%%