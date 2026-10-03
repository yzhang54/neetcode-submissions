class Solution:
    def numSquares(self, n: int) -> int:
        
        # n = 0: 0
        # n = 1: 1 -> base 
        # n = 2: 2 -> dp[1] + dp[1]
        # n = 3: 3 -> dp[2] + dp[1], or dp[1] + dp[1] + dp[1]
        # n = 4: 4 -> 1
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for num in range(1, n+1):
            root = int(math.sqrt(num))
            for i in range(1, root+1):
                square = i * i
                dp[num] = min(1 + dp[num - square], dp[num])
        
        return dp[n]


            
