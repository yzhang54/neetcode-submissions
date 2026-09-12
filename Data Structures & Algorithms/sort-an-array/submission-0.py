class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def merge(nums):
            if len(nums) == 1:
                return nums

            mid = len(nums)//2

            nums1 = merge(nums[:mid])
            nums2 = merge(nums[mid:])

            return sort(nums1, nums2)

        def sort(nums1, nums2):
            res = []
            p1= 0
            p2 = 0

            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    res.append(nums1[p1])
                    p1 += 1
                else:
                    res.append(nums2[p2])
                    p2 += 1

            while p1 < len(nums1):
                res.append(nums1[p1])
                p1 += 1
            while p2 < len(nums2):
                res.append(nums2[p2])
                p2 += 1

            return res
        
        return merge(nums)