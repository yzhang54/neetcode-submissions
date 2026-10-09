class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [] # max heap: freq:letter

        if a != 0:
            heapq.heappush(heap, [-a, "a"])

        if b != 0:
            heapq.heappush(heap, [-b, "b"])
        
        if c != 0:
            heapq.heappush(heap, [-c, "c"])

        res = ""
        while heap:
            print(heap)
            negFreq, letter = heapq.heappop(heap)
            if heap and len(res) >=2 and res[-2:] == letter * 2:
                print("test1")
                negFreq2, letter2 = heapq.heappop(heap)
                res += letter2
                negFreq2 += 1

                heapq.heappush(heap, [negFreq, letter])
                if negFreq2 == 0:
                    continue
                heapq.heappush(heap, [negFreq2, letter2])
            elif (len(res) >=2 and res[-2:] != letter * 2) or len(res) < 2:
                print("test2")
                res += letter 
                negFreq += 1

                if negFreq == 0:
                    continue

                heapq.heappush(heap, [negFreq, letter])

        return res

