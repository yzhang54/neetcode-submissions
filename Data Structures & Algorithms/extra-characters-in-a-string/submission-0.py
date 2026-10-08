class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        memo = defaultdict(int)
        dictionarySet = set(dictionary)
        def dfs(start):
            if start == len(s):
                return 0
            if start in memo:
                return memo[start]
            res = len(s)
            for end in range(start, len(s)):
                if s[start:end+1] in dictionarySet:
                    res = min(res, dfs(end+1))
                else:
                    res = min(res, end - start + 1 + dfs(end+1))

            memo[start] = res
            return res

        return dfs(0)