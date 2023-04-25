#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# 96% 56%

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return
        
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        elif left and not right:
            return left
        elif right and not left:
            return right
        else:
            return
#############################################################
#%%
# first solution 5% 5%

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_path = []
        self.q_path = []
        self.p_found = False
        self.q_found = False
        res =  self.dfs(root,p,q)
        for i,j in zip(self.p_path,self.q_path):
            if i.val == j.val:
                lca = i
            else:
                break
        return lca
    
    def dfs(self,root,p,q,path = None):
        if root is None:
            return
        if path is None:
            path = []
        x = [i.val for i in path]
        if root.val == p.val:
            self.p_path = [i for i in path] + [root]
            self.p_found = True
        elif root.val == q.val:
            self.q_path = [i for i in path] + [root]
            self.q_found = True

        if self.p_found and self.q_found:
            #FOUND BOTH, returning
            return True
        
        path.append(root)
        
        res = self.dfs(root.left,p,q,path)
        #returning from left
        if res:
            return True
        res = self.dfs(root.right,p,q,path)
        if res:
            return True
        #not left nor right
        path.pop()
        return False
        
