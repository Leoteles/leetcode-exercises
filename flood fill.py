#https://leetcode.com/problems/flood-fill/
from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows= len(image)
        cols= len(image[0])
        color_to_replace  = image[sr][sc]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        stack = deque([[sr,sc]])
        visited = set()
        while stack:
            i,j = stack.popleft()
            #print('iter',i,j)
            if (i,j) in visited:
                #Alredy visited
                continue

            visited.add((i,j))
            
            if image[i][j] == color_to_replace:
                image[i][j] = color
            else:
                continue
            
            for direction in directions:
                next_i,next_j = i + direction[0],j + direction[1]
                if (0 <= next_i < rows) and (0 <= next_j < cols):
                    stack.append([next_i,next_j])
            #print(stack)
        return image
image = [[1,1,1],[1,1,0],[1,0,1]]
Solution().floodFill(image)

#%%



