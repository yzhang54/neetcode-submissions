class Solution:
    def reorganizeString(self, s: str) -> str:
        # 这道题我想的是
        # 先把 s frequency count, and then put them into a max heap [freq, letter], we pop each time , and comapre it the char has appeared before. and then we put it into queue, queue store elements that are not ready yet. when the front of queue has not appeared in the output before, we put it back to the heap 

        counter = Counter(s)

        heap = []
        for char, freq in counter.items():
            heapq.heappush(heap, [-freq, char])

        res = ""
        q = []
        while heap:
            freq, char = heapq.heappop(heap)

            # duplicate adj chars
            if len(res) >= 1 and res[-1] == char:
                q.append([freq, char])
            # not duplicate 
            else:
                freq += 1
                res += char

                if freq != 0:  
                    q.append([freq, char])

            
            while q and q[0][1] != char:
                qFreq, qChar = q.pop()
                heapq.heappush(heap, [qFreq, qChar])

        # print(res)
        # return res
        return res if len(res) == len(s) else ""

