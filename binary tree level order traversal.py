# https://leetcode.com/problems/binary-tree-level-order-traversal/

#Solution 30% 17%
from collections import deque
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = [[root.val]]
        stack = deque((root.left,root.right))
        level  = []
        len_level = len(stack)

        while stack:
            node = stack.popleft()
            len_level -= 1
            if node:
                level.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            if not len_level and level:
                out.append(level)
                #Go to next level
                level = []
                len_level = len(stack)
        return out


#Solution using a for loop on the stack to separate levels on bfs
from collections import deque
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return root
        queue = []
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            l = len(queue)
            for l in range(l):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            return_list.append(ans)
        return return_list
            