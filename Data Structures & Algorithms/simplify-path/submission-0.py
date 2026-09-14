class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # defination: stack stores each valid dir name 
        # pop: if curChars == ".."
        # push: if curChars == "/"
        stack = []

        path = path.split("/")

        # print(path)
        for i in range(len(path)):
            if path[i] == "" or path[i] == "." or (path[i]== ".." and not stack):
                continue

            if stack and path[i] == "..":
                stack.pop()
            else:
                stack.append(path[i])

        print(stack)
        res = "/" + "/".join(stack)
        return res
            


