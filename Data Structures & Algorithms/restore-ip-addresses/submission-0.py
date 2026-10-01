class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # four integers, each between 0 - 255, 0 is valid, but not leading 0s. 
        res = []
        def dfs(i, curIP):
            # base
            if len(curIP) == 4 and i == len(s):
                res.append(".".join(curIP))
                return 
            
            if i >= len(s) or len(curIP) > 4:
                return 
            
            # print(i)
            # print(curIP)
            # next choices 
            for end in range(i, len(s)):
                print(s[i:end+1])
                # print(end)
                # print(i)
                # print("----")
                # single digit
                if end - i + 1 == 1:
                    curIP.append(s[i:end+1])
                    dfs(end+1, curIP)
                    curIP.pop()

                # multi-digits
                if end - i + 1 > 1:
                    # we have leading 0s
                    if s[i] == "0" or not (0 <= int(s[i:end+1]) <= 255):
                        return 
                    curIP.append(s[i:end+1])
                    dfs(end+1, curIP)
                    curIP.pop()

        
        dfs(0, [])
        return res