class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        res = 0
        resStr = ""
        for strLen in range(1, len(s)+1):
            for left in range(len(s) - strLen+1):
                right = left + strLen - 1
                if strLen == 1:
                    dp[left][right] = True
                elif strLen == 2 and s[left] == s[right]:
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left+1][right-1] and s[left] == s[right]

                if dp[left][right] and res < right-left+1:
                    res = max(res, right-left+1)    
                    resStr = s[left:right+1]


        return resStr
