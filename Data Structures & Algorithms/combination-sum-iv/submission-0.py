class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = defaultdict(int) # curSum: freq
        def dfs(curSum):
            if curSum == target:
                return 1
            if curSum > target:
                return 0
            if curSum in memo:
                return memo[curSum]

            res = 0
            for i in range(len(nums)):
                res += dfs(curSum+nums[i])

            memo[curSum] = res
            return memo[curSum]

        return dfs(0)