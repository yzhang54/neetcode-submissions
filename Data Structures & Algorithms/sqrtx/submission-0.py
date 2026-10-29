class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x
        ans = None 
        while left <= right:
            mid = (left+right)//2

            if mid * mid == x:
                return mid 
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans if ans != None else 0