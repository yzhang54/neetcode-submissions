class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo =  defaultdict(int)
        def dfs(start1, start2):
            
            if start1 == len(word1):
                return len(word2) - start2
            if start2 == len(word2):
                return len(word1) - start1

            if (start1, start2) in memo:
                return memo[(start1, start2)]
            


            cur = float("inf")
            if word1[start1] != word2[start2]:
                # replace, insert, delete
                cur = 1+ min(dfs(start1+1, start2+1), dfs(start1, start2+1), dfs(start1+1, start2))
            else:
                cur = min(cur, dfs(start1+1, start2+1))

            memo[(start1, start2)] = cur 
            return memo[(start1, start2)]

        return dfs(0,0)