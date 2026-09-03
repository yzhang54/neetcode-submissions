class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 这道题 其实我觉得是bottom down. 因为 它依赖之前的状态 但是 我不知道怎么写 所以用dfs, 但是用 dfs 我有点不知道怎么用memo
        self.dp = {} # at day i, the max profit we can get
        self.res = 0
        def dfs(index, holdStock, canBuy):
            if (index, holdStock, canBuy) in self.dp:
                return self.dp[(index, holdStock, canBuy)]
            if index == len(prices):
                return 0

            # have stock, cant buy
            if holdStock == True and canBuy == False:
                # 1. skip, keep holding
                # 2. sell current stock
                profitOne = dfs(index+1, True, False)
                profitTwo = dfs(index+1, False, False) + prices[index]
                self.dp[(index, holdStock, canBuy)] = max(profitOne, profitTwo)
            # no stock, but can't buy
            elif holdStock == False and canBuy == False:
                self.dp[(index, holdStock, canBuy)]  = dfs(index+1, True, True)
            # no stock, can buy
            else: 
                # 1. buy stock or don't buy
                profitOne = dfs(index+1, True,False) - prices[index]
                profitTwo = dfs(index+1, False, True)
                self.dp[(index, holdStock, canBuy)] = max(profitOne, profitTwo)

            return self.dp[(index, holdStock, canBuy)]

        dfs(0, False, True)
        return self.dp[(0, False, True)]

