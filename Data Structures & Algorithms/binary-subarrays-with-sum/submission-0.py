class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1

        res = 0
        curGoal = 0
        for i in range(len(nums)):
            curGoal += nums[i]

            if curGoal - goal in prefix:
                res += prefix[curGoal - goal]

            prefix[curGoal] += 1

        return res