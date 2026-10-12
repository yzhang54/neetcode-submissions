class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        def canMeetFreq(freq):
            print("freq", freq)
            start = 0
            for end in range(len(nums)):

                if end - start + 1 == freq:
                    require = nums[end]
                    operations = 0
                    for i in range(start, end+1):
                        operations += require - nums[i]
                        # print("operation", operations)
                    print("start", start)
                    print("end", end)
                    print("operations", operations)
                    if operations <= k:
                        return True

                    start += 1

            return False

        left = 1
        right = len(nums) 
        ans = 0
        while left <= right:
            # the current freq
            mid = (left+right)//2
            if canMeetFreq(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


