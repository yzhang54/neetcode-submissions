class Solution:
    def numDecodings(self, s: str) -> int:
        
        # this way use top down better cuz we have an entire string, which is an big problem, using dfs is better for us to break down the problem, and this is 1dp cuz we only need index to solve this problem.

        self.memo = {}
        def dfs(index): #def: from index, we have n number of ways to break down the string[index:]
            #base
            if index in self.memo:
                return self.memo[index]

            if index >= len(s):
                return 1

            #other options
            # 我有点不知道当0 的时候该怎么处理。我知道这不是个valid的choice 但是不知道代码该怎么写， 我想的是这种情况那么整条线路就不合法 
            if s[index] == "0":
                return 0
            res = dfs(index+1)
            if index+2 <= len(s) and int(s[index:index+2]) <= 26:
                res += dfs(index+2)

            self.memo[index] = res
            
            return self.memo[index]

        return dfs(0)