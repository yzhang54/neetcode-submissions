class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num, prevOps = 0, "+"
        s += "+"
        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i].isdigit():
                num = num*10 + int(s[i])
            else:
                if prevOps == "+":
                    stack.append(int(num))
                elif prevOps == "-":
                    stack.append(-int(num))
                elif prevOps == "*":
                    stack[-1] = stack[-1] * num
                elif prevOps == "/":
                    stack[-1] = int(stack[-1] / num)

                prevOps = s[i]
                num = 0
            
            print(prevOps)
            print(num)

        return sum(stack)

