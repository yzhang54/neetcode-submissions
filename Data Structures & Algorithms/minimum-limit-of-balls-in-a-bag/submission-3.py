class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def canReduce(curSize):
            operations = 0
            for num in nums:
                operations += (num - 1) // curSize

            return operations <= maxOperations

        left, right = 1, max(nums)
        ans = None 
        while left <= right:
            mid = (left+right)//2

            if canReduce(mid):
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1

        return ans
        

