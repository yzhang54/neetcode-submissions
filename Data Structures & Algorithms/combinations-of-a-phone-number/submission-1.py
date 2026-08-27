class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        self.digitToLetters = {
            "2": {"a", "b", "c"}, 
            "3": {"d", "e", "f"}, 
            "4": {"g", "h", "i"}, 
            "5": {"j", "k", "l"}, 
            "6": {"m", "n", "o"}, 
            "7": {"p", "q", "r", "s"}, 
            "8": {"t", "u", "v"}, 
            "9": {"w", "x", "y", "z"}
        }
        self.res = []
        def backtrack(index, tmp):
            if index >= len(digits):
                self.res.append("".join(tmp))
                return 

            curNum = digits[index]
            for letter in self.digitToLetters[curNum]:
                tmp.append(letter)
                backtrack(index+1, tmp)
                tmp.pop()

        backtrack(0,[])
        return self.res

