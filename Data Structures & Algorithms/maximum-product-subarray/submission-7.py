class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [[1, 1] for _ in range(len(nums))] # dp[i] = [(min, max)]: until i, the max subarray we can get
        res = float("-inf")
        # bottom up, 1d dp
        for index in range(len(nums)):
            curNum = nums[index]
            if index >= 1:
                minProduct, maxProduct = dp[index-1]
                curMin, curMax = min(curNum, minProduct * curNum, maxProduct * curNum), max(curNum, minProduct * curNum, maxProduct * curNum)
                dp[index] = [curMin, curMax]
                res = max(res, curMax)
            else:
                dp[index] = [curNum, curNum]
                res = max(res, curNum)

        return res
        
        