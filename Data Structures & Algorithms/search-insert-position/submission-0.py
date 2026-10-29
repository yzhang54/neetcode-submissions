class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        ans = None

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans if ans != None else len(nums) 