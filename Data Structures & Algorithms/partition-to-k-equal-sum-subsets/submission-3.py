class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # if sum(nums)//k
        equalSum = sum(nums)//k
        buckets = [0] * k
        memo = set()
        def dfs(i):
            state = (i,tuple(sorted(buckets)))
            if state in memo:
                return False 
            if i == len(nums):
                return True

            for j in range(k):
                if buckets[j] + nums[i] <= equalSum:
                    buckets[j] += nums[i]
                    if dfs(i+1):
                        return True
                    buckets[j] -= nums[i]

            memo.add(state)
            return False

        return dfs(0)


