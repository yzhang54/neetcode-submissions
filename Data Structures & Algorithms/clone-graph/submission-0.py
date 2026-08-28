"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        self.oldToNew = defaultdict(Node)
        def dfs(node):
            if node in self.oldToNew:
                return self.oldToNew[node]
            if not node:
                return None

            # 在这一层我创建 node。下一层我走 邻居
            copyNode = Node(node.val)
            self.oldToNew[node] = copyNode

            for n in node.neighbors:
                copyNode.neighbors.append(dfs(n))

            # self.visited.remove(node)
            return copyNode
        
        return dfs(node)
