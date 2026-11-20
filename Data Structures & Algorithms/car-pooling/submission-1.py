class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        inHeap = []
        outHeap = []

        for trip in trips:
            numPassengers, fromTime, toTime = trip
            heapq.heappush(inHeap, [fromTime, numPassengers])
            heapq.heappush(outHeap, [toTime, numPassengers])

        curCap = 0
        while inHeap and outHeap:
            # print("inHeap", inHeap)
            # print("outHeap", outHeap)
            # print("curCap", curCap)
            if inHeap[0][0] < outHeap[0][0]:
                _, numPassengers = heapq.heappop(inHeap)
                curCap += numPassengers
            elif inHeap[0][0] > outHeap[0][0]:
                _, numPassengers = heapq.heappop(outHeap)
                curCap -= numPassengers
            else:
                _, numPassengers = heapq.heappop(inHeap)
                curCap += numPassengers
                _, numPassengers = heapq.heappop(outHeap)
                curCap -= numPassengers

            if curCap > capacity:
                return False
        # while outHeap:

        return True

