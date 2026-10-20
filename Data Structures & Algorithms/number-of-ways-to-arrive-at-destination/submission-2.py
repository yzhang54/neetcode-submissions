class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        heap = []
        distance = [float("inf")] * n
        distance[0] = 0
        graph = defaultdict(list)
        ways = [0] * n
        ways[0] = 1

        for u,v,time in roads:
            graph[u].append((v,time))
            graph[v].append((u,time))

        heapq.heappush(heap, (0, 0))
        while heap:
            time, node = heapq.heappop(heap)

            if time > distance[node]:
                continue
            for nextNode, weight in graph[node]:
                    newTime = time + weight
                    if newTime < distance[nextNode]:
                        heapq.heappush(heap, (newTime, nextNode))
                        distance[nextNode] = newTime
                        ways[nextNode] = ways[node] 
                    elif newTime == distance[nextNode]:
                        ways[nextNode] += ways[node]
        
        return ways[-1] % (10**9 + 7)
