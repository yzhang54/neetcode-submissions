class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
            
        lLeft, lRight = 0, len(nums)-1

        while lLeft < lRight:
            mid = (lLeft+lRight)//2

            if nums[mid]>=target:
                lRight = mid
            else:
                lLeft = mid + 1

        if nums[lLeft] != target:
            return [-1, -1]

        rLeft, rRight = 0, len(nums)-1

        while rLeft < rRight:
            mid = (rLeft+rRight+1)//2

            if nums[mid] <= target:
                rLeft = mid 
            else:
                rRight = mid - 1
        
        return [lLeft, rLeft] 
        