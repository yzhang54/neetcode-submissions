class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums = [float("-inf")] + nums + [float("-inf")]
        left, right = 1, len(nums)-2

        print(nums)
        while left <= right:
            mid = (left+right)//2
            
            print(mid)
            print(nums[mid])
            if nums[mid-1] <= nums[mid] >= nums[mid+1]:
                return mid - 1
            # go right
            elif nums[mid-1] <= nums[mid] <= nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1


        return -1
