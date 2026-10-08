class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = defaultdict(int)
        def dfs(start, end):
            if start > end:
                return 0
            if (start,end) in memo:
                return memo[(start,end)]
            curMax = 0
            # take left
            curMax = max(piles[start] - dfs(start+1, end), piles[end] - dfs(start, end-1))

            memo[(start,end)] = curMax

            return memo[(start,end)]

        return True if dfs(0, len(piles)-1) > 0 else False
