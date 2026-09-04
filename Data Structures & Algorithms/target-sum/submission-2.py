class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {} # sum: #ways
        def dfs(index, curSum):
            #base
            if index >= len(nums):
                return 1 if curSum == target else 0
            if (index, curSum) in self.memo:
                return self.memo[(index, curSum)]

            #next choice 
            plusFreq = dfs(index+1, curSum + nums[index])
            minusFreq = dfs(index+1, curSum - nums[index])

            self.memo[(index, curSum)] = plusFreq + minusFreq

            return self.memo[(index, curSum)]

        return dfs(0, 0)
