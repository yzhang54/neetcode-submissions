class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = [] # max heap log n push pop

        counter = Counter(nums)

        for value, freq in counter.items():
            heapq.heappush(heap, [-freq, value])

        res = []
        while heap:
            negFreq, value = heapq.heappop(heap)

            res.append(value)
            if len(res) == k:
                break
        
        return res