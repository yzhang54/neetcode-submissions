class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1} # sum: freq
        curSum = 0
        res = 0
        for num in nums:
            curSum += num
            if curSum - k in prefix:
                res += prefix[curSum-k]

            if curSum not in prefix:
                prefix[curSum] = 0
            prefix[curSum] += 1

        return res


