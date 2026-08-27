class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        def backtrack(path, start):
            self.res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue 
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()

        backtrack([], 0)
        return self.res