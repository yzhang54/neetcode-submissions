class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heap = stones
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                continue
            else:
                newStone = -abs(x-y)
                heapq.heappush(heap, newStone)
        
        return -heap[0] if len(heap) == 1 else 0


        