class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up: cuz we already know the small problem (single coin) to the big problem the target amount

        dp = [0]*(amount+1) # index:amount val:#ways
        for money in range(1, amount+1):
            res = float("inf")
            # 我现在卡的点是 怎么用loop 去 表达different combination of coins 
            for coin in coins:
                if money - coin >= 0:
                    res = min(res, dp[money - coin]+1)
            
            dp[money] = res
        
        print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1