class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = [] # [val, freq]
        # push: once we meet different val than curVal we push in curVal, curFreq
        # pop: if cur == top val and (1+prevFreq) == k, we pop


        for i in range(len(s)):

            cur = s[i]

            # stack empty ?
            if len(stack) == 0:
                stack.append([cur, 1])
            
            elif cur == stack[-1][0]:
                stack[-1][1] += 1
            
            elif cur != stack[-1][0]:
                stack.append([cur, 1])

            if stack and stack[-1][1] == k:
                stack.pop()
            # after count changes, did it reach k?

        print(stack)
        res = ""
        for val, freq in stack:
            res += freq * val

        return res


