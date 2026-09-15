class Solution:
    def decodeString(self, s: str) -> str:
        # pop when we see ]
        # push when we see [
        
        stack = []
        curStr, curNum = "", ""
        res = ""

        for i in range(len(s)):

            cur = s[i]

            if cur == "[":
                stack.append([curStr, int(curNum)])
                curStr, curNum = "", ""
            elif cur == "]":
                prevStr, prevNum = stack.pop()
                curStr = prevStr + prevNum * curStr
            else:
                if cur.isdigit():
                    curNum += cur
                else:
                    curStr += cur

        return curStr