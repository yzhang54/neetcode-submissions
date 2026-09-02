class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #dp[i]: the longest increasing subsequence up to index i, base:1
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)