class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.res = []
        # how to talk bout this question in interview: each level, i would trying different strings starting from index start, and next level, the index will start from (start+lastEnd), we would search all possible substrings. 
        def isPali(startIndex, endIndex):
            subString = s[startIndex:endIndex]
            # print(subString)
            # print(subString == subString[::-1])
            return subString == subString[::-1]

        def backtrack(start, tmp):
            if start >= len(s):
                self.res.append(tmp[:])
                return 

            
            for i in range(start, len(s)):
                if isPali(start, i+1):
                    tmp.append(s[start:i+1])
                    backtrack(i+1, tmp)
                    tmp.pop()

        backtrack(0, [])
        return self.res



