class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        left = 0
        right = len(arr) - 1

        def helper(startIndex):
            endIndex = startIndex + k - 1
            rightWindowEndIndex = endIndex + 1

            # not valid window, we need to move to left
            if rightWindowEndIndex >= len(arr):
                return True
            print("rightWindowEndIndex", rightWindowEndIndex)
            # print("abs(arr[startIndex] - x) < abs(arr[rightWindowEndIndex] - x)", abs(arr[startIndex] - x) < abs(arr[rightWindowEndIndex] - x))
            # print("abs(arr[startIndex] - x) == abs(arr[rightWindowEndIndex] - x)", abs(arr[startIndex] - x) == abs(arr[rightWindowEndIndex] - x))
            # print("arr[startIndex] < arr[rightWindowEndIndex])", arr[startIndex] < arr[rightWindowEndIndex])
            # compare the current window and the window on the right
            if abs(arr[startIndex] - x) < abs(arr[rightWindowEndIndex] - x) or (abs(arr[startIndex] - x) == abs(arr[rightWindowEndIndex] - x) and arr[startIndex] < arr[rightWindowEndIndex]):
                print("helper return True")
                return True
            print("helper return False")
            return False

        ans = 0 
        while left <= right:
            # the starting of sliding window that is closest to x
            mid = (left+right)//2
            print("mid", mid)
            if helper(mid):
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1

        print(ans)
        return arr[ans:ans+k]