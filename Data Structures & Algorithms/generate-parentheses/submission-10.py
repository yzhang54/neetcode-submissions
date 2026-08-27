class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        # i know the code pattern but not sure what to select/not select
        def backtrack(openP, closeP, tmp):
            if closeP == n:
                self.res.append("".join(tmp))
                return 

            # select
            if openP < n:
                tmp.append("(")
                backtrack(openP+1, closeP, tmp)
                tmp.pop()
            # not select
            if openP > closeP:
                tmp.append(")")
                backtrack(openP, closeP+1, tmp)
                tmp.pop()

        backtrack(0, 0, [])
        return self.res