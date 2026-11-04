class Solution:
    def decodeString(self, s: str) -> str:
        # pop when we see ]
        # push when we see [
        
        stack = [] # ("", k)
        curDigit = 0
        curChar = ""
        for char in s:

            if char == "[":
                stack.append([curChar, curDigit])
                curDigit = 0
                curChar = ""
            elif char == "]":
                prevChar, multiple = stack.pop()
                curChar = prevChar + multiple * curChar
            elif char.isdigit():
                curDigit = curDigit*10 + int(char)
            else:
                curChar += char

        return curChar
