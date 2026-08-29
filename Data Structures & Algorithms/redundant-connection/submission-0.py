class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find: helps to connect nodes together with no cycle

        parent = {i+1: i+1 for i in range(len(edges))}
        print(parent)
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])

            return parent[node]

        def union(node1, node2):

            rootA = find(node1)
            rootB = find(node2)

            if rootA == rootB:
                return False

            parent[rootA] = rootB
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]

        print(parent)
        