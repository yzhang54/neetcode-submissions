"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 1:
            return Node(grid[0][0], True, None, None, None, None)
        
        if len(grid) < 1:
            return None
        

        curVal = grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if curVal != grid[row][col]:
                    gridSize = len(grid)//2

                    # print("----")
                    # print(gridSize)
                    # print(grid)
                    # print(grid[:gridSize])
                    # print(grid[:gridSize][:gridSize])
                    # print(grid[:gridSize][gridSize:])
                    # print(grid[gridSize:][:gridSize])
                    # print(grid[gridSize:][gridSize:])
                    topLeftNode = self.construct([row[:gridSize] for row in grid[:gridSize]])
                    topRightNode = self.construct([row[gridSize:] for row in grid[:gridSize]])
                    bottomLeftNode = self.construct([row[:gridSize] for row in grid[gridSize:]])
                    bottomRightNode = self.construct([row[gridSize:] for row in grid[gridSize:]])

                    return Node(0, False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)

        
        return Node(grid[0][0], True, None, None, None, None)