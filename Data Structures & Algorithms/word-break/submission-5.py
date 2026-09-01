class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dictSet = set(wordDict)
        # top down dp
        self.memo = [None] * len(s)
        def dfs(start):
            if start == len(s):
                return True
            if self.memo[start] != None:
                return self.memo[start]

            for end in range(start, len(s)):
                curWord = s[start:end+1]
                if curWord in dictSet:
                    if dfs(end+1):
                        self.memo[start] = True
                        return True

            self.memo[start] = False

            return self.memo[start]
        return dfs(0)

            
