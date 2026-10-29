class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # [[-5,5],[-2,1],[0,3]]
        # [-2,1] [0,3] [-5,5]
        points.sort(key=lambda x:(x[1]))

        intersect = points[0]
        res = 1
        for i in range(1, len(points)):
            # overlap
            if points[i][0] <= intersect[1]:
                intersect = [min(intersect[0], points[i][0]),min(intersect[1], points[i][1])]
            # non-overlap
            else:
                res += 1
                intersect = points[i]
        
        return res
