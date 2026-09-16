class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        # 最先进去的 最快出来: 如果当前building 比之前的building要高 说明看不见occean 这个时候就可以出来了

        stack = [] # (height, index)
        for i in range(len(heights)):
            curBuilding = heights[i]
            while stack and stack[-1][0] <= curBuilding:
                stack.pop()

            stack.append([curBuilding, i])
        
        res = []
        for _, i in stack:
            res.append(i)
        # sort result in increasing order 
        # res.sort()

        return res 
