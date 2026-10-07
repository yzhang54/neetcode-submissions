"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key=lambda interval: (interval.start))

        heap = [] # min heap: endMeetingTime, it keeps the record of the current running meetings, we finish the ealiest meeting based on the smaller end time, and pop it off from the heap

        res = 0
        for i in range(len(intervals)):
            curTime = intervals[i].start
            while heap and heap[0] <= curTime:
                heapq.heappop(heap)

            heapq.heappush(heap, intervals[i].end)
            res = max(res, len(heap))

        return res

