class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stackS = []
        for char in s:
            if char == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(char)

        stackT = []
        for char in t:
            if char == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(char)

        
        return "".join(stackS) == "".join(stackT)