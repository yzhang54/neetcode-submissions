class Solution:
    def integerBreak(self, n: int) -> int:
        # 0: 0 
        # 1: 1 -> 1
        # 2: 1 + 1 -> 1*1
        # 3: 1 + 2 -> 1*2 1+1+1 -> 1*1*1
        # 4: 2 + 2 -> 2*2
        # max(1 + dp[num-i], dp[num])
        # max product we get for current n
        dp = [0] * (n+1)
        dp[1] = 1
# 3-1 = 1 3-2 = 1
        for num in range(1, n+1):
            # i think how i break down the number is wrong 
            for i in range(1, num+1):
                dp[num] = max(i*dp[num-i], dp[num], i * (num-i))

        print(dp)

        return dp[num]

            

