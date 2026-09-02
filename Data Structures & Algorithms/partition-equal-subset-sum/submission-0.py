class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        halfSum = sum(nums)//2
        self.dp = [None] * (halfSum+1) # amount:
        def dfs(target, start):
            # if any of the ununsed nums can make up to target
            if self.dp[target] != None:
                return self.dp[target]
            if target == 0:
                return True
            if target < 0:
                return False
            if start >= len(nums):
                return False
            
            for i in range(start, len(nums)):
                if dfs(target - nums[i],i+1):
                    self.dp[target - nums[i]] = True
                    return True

            self.dp[target] = False
            return self.dp[target]
        return dfs(halfSum, 0)