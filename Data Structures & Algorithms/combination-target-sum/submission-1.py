class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def backtrack(curSum, path, start):
            if curSum == target:
                self.res.append(path[:])
                return 

            if curSum > target:
                return 

            # 我疑惑的点是 start 控制选数字的顺序， 控制重复数字 但是我需要的是数字可以重复 但是combination 不能重复。 那这个怎么靠start来控制呢
            for index in range(start, len(nums)):
                num = nums[index]
                path.append(num)
                backtrack(curSum + num, path, index)
                path.pop()

        backtrack(0,[], 0)
        return self.res