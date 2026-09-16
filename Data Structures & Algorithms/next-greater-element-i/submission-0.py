class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []  #[val, index]
        res = [-1] * len(nums2)
        # if stack[-1] < curVal: pop 如果找到了 next greater element

        for i in range(len(nums2)):

            while stack and stack[-1][0] < nums2[i]:
                _, index = stack.pop()
                res[index] = nums2[i]

            stack.append([nums2[i], i])

        print(res)
        output = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    output.append(res[j])

        
        return output