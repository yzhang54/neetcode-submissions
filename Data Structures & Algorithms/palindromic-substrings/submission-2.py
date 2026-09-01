class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        # bottom up: small problem -> big problem
        dp = [[False] * len(s) for _ in range(len(s))] # state: for s[left, right] the max number of substring, which is palindromes
        for strLen in range(1, len(s)+1):
            for left in range(len(s)-strLen+1):
                right = left + strLen - 1

                if strLen == 1:
                    dp[left][right] = True
                elif strLen == 2:
                    dp[left][right] = s[left] == s[right]
                else:
                    dp[left][right] = s[left] == s[right] and dp[left+1][right-1]

                if dp[left][right]:
                    res += 1

        
        return res

