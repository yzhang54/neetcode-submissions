class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # include if the curSum increases, not take the current value 

        res = nums[0]
        curSum = nums[0]
        for index in range(1, len(nums)):
            num = nums[index]
            curSum = max(curSum+num, num)
            res = max(res, curSum)

        return res