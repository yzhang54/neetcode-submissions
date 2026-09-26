class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
            
        mapping = defaultdict(list) # {1:[2, 3]}
        degree = [0] * n
        for n1, n2 in edges:
            mapping[n1].append(n2)
            mapping[n2].append(n1)
            degree[n1] += 1
            degree[n2] += 1

        q = deque()
        remaining = n
        for i in range(len(degree)):
            if degree[i] == 1:
                q.append(i)


        # print(mapping)
        # print(degree)
        # print(q)
        while remaining > 2:
            remaining -= len(q)
            for _ in range(len(q)):
                curNode = q.popleft()
                for nextNode in mapping[curNode]:
                    degree[nextNode] -= 1
                    if degree[nextNode] == 1:
                        q.append(nextNode)

        return list(q)