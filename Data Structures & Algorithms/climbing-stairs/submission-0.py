class Solution:
    def climbStairs(self, n: int) -> int:
        
        self.memo = {}
        def dfs(n):
            if n in self.memo:
                return self.memo[n]
            if n == 0 :
                return 1
            if n < 0:
                return 0

            

            res = dfs(n-1) + dfs(n-2)
            self.memo[n] = res
            return res

        dfs(n)
        return self.memo[n]