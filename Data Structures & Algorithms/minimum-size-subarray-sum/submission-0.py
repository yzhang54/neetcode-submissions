class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLen = float("inf")
        curWindowSum = 0
        left = 0

        for right in range(len(nums)):
            # the logic is that we keep adding right vals, and each time we check if the current total sum is greater than target, and we records. at the same time, we shrink the left bc we wanna keep the min len of the subarray. the window is valid when the sum is >= target but minimal length
            curWindowSum += nums[right]

            while curWindowSum - nums[left] >= target:
                curWindowSum -= nums[left]
                left += 1

            if curWindowSum >= target:
                print(left)
                print(right)
                print(minLen)
                minLen = min(minLen, right - left + 1)

        return minLen if minLen != float("inf") else 0

