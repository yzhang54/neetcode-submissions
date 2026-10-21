"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        copyMapping = defaultdict(list) # node:[nei]
        copyMapping[None] = None
        def dfs(curNode):
            if not curNode:
                return None
            if curNode in copyMapping:
                return copyMapping[curNode]

            copyNode = Node(curNode.val)
            copyMapping[curNode] = copyNode

            for nei in curNode.neighbors:
                copyNode.neighbors.append(dfs(nei))


            return copyMapping[curNode]

        dfs(node)
        return copyMapping[node]