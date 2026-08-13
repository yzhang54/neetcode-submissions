class Solution:
    def findMin(self, nums: List[int]) -> int:
        # first True FFFTTT
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] > nums[-1]: # make this False 
                left = mid + 1 
            else:
                right = mid - 1 
        
        return nums[left]

