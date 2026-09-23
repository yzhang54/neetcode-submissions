class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        def canPairs(difference):
            pairs = 0

            i= 0
            while i < len(nums)-1:
                diff = abs(nums[i] - nums[i+1])
                if diff > difference:
                    i += 1
                else:
                    pairs += 1
                    i += 2

            return pairs >= p

        while left < right:
            mid = (left+right)//2

            if canPairs(mid):
                right = mid 
            else:
                left = mid + 1

        return left 