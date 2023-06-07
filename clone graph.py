#https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#Solution 69% 8%
class Solution(object):
    
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        visited = {node.val:Node(node.val)}
        q = [node]
        while q:
            this_node = q.pop(0)
            this_node_clone = visited[this_node.val]

            for i in this_node.neighbors:
                if i.val not in visited:
                    visited[i.val] = Node(i.val)
                    q.append(i)
                this_node_clone.neighbors.append(visited[i.val])


        return visited[node.val]

#%%
#DFS Solution 11% 6%
class Solution:
    visited = None
    def cloneGraph(self, node: 'Node') -> 'Node':
        if self.visited is None:
            self.visited = {}
        if not node:
            return
        if node.val in self.visited:
            return
        #Create node
        self.visited[node.val] = Node(val=node.val)
        #Add neighbours to node
        for nei in node.neighbors:
            if nei.val in self.visited:
                self.visited[node.val].neighbors.append(self.visited[nei.val])
            else:
                self.visited[node.val].neighbors.append(self.cloneGraph(nei))
            
        return self.visited[node.val]