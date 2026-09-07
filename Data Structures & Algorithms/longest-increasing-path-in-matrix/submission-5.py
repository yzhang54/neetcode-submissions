class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # i don't think we need an visited set here cuz we already have memo
        self.memo = {} # (row, col, val): # num
        def dfs(i,j, prevVal):
            # find the longest increasing path starting (i,j)
            # base case: 1. out of range. 2. not increasing 
            if i not in range(len(matrix)) or j not in range(len(matrix[0])):
                return 0
            if not (prevVal < matrix[i][j]):
                return 0
            
            if (i,j, prevVal) in self.memo:
                return self.memo[(i,j,prevVal)]

            # next choices
            # four directions 
            res = max(dfs(i+1, j, matrix[i][j]), dfs(i, j+1, matrix[i][j]), dfs(i-1, j, matrix[i][j]), dfs(i, j-1, matrix[i][j])) + 1 

            # print(self.memo)

            self.memo[(i,j, prevVal)] = res 

            return res

        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans = max(ans, dfs(row, col, -1))

        return ans

# [7,7,5],
# [2,4,6],
# [8,2,0]