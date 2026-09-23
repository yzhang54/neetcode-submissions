class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity):
            curDays = 1
            curPack = 0
            for i in range(len(weights)):
                if curPack + weights[i] > capacity:
                    curDays += 1
                    curPack = 0

                curPack += weights[i]

            return curDays <= days

        left, right = max(weights), sum(weights)
        # least weight capacity means max days under DAYS
        while left < right:
            mid = (left+right) // 2

            if canShip(mid):
                right = mid 
            else:
                left = mid + 1

        return left
