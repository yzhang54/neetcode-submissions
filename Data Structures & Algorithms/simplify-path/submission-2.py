class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")
        stack = []
        for cur in path:
            if cur == "":
                continue 
            if not stack and (cur == ".." or cur == "."):
                continue
            if stack and cur == "..":
                stack.pop()
            elif stack and cur == ".":
                continue
            else:
                stack.append(cur)

        return "/" + "/".join(stack)


