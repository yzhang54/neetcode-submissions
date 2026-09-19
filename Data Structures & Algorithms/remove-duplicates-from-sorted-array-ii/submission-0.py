class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        read = 0
        write = 0
# read  0 -> 3, 3 -> 5, 5
# write 0 -> 2, 2 -> 4, 4
# group 0 -> 2, 3 -> 4, 5
        while read < len(nums):
            groupStart = read
            while groupStart + 1 < len(nums) and nums[groupStart] == nums[groupStart+1]:
                groupStart += 1

            if groupStart - read + 1 >= 2:
                nums[write] = nums[read]
                write += 1
                nums[write] = nums[read]
                write += 1
            # nums is 1 length 
            else:
                nums[write] = nums[read]
                write += 1

            read = groupStart + 1
            print(nums)

        return write 