class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # max heap
        self.rightHeap = [] # min heap 

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.leftHeap, -num)
        if len(self.leftHeap) - len(self.rightHeap) > 1:
            transfer = heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, -transfer)

        if self.leftHeap and self.rightHeap and (-self.leftHeap[0]) > self.rightHeap[0]:
            leftNum = -heapq.heappop(self.leftHeap)
            rightNum = heapq.heappop(self.rightHeap)

            heapq.heappush(self.leftHeap, -rightNum)
            heapq.heappush(self.rightHeap, leftNum)

    def findMedian(self) -> float:
        
        # odd
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        # even 
        else:
            return (-self.leftHeap[0] + self.rightHeap[0])/2
        