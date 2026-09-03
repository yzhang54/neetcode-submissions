class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            if i > 0 and max(res[-1][0], intervals[i][0]) <= min(res[-1][1], intervals[i][1]):
                start, end = res.pop()
                new = [min(start, intervals[i][0]), max(end, intervals[i][1])]
                res.append(new)
                continue
            res.append(intervals[i])

        return res