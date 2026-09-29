class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastAppear = defaultdict(int)
        for i in range(len(s)):
            curChar = s[i]
            lastAppear[curChar] = i
        print(lastAppear)
        res = []
        start = 0
        resChar,resEnd = "", 0
        for end in range(len(s)):
            # print(start)
            # print(end)
            if resChar != s[end]:
                if resEnd >lastAppear[s[end]]:
                    continue
                else:
                    resChar = s[end]
                    resEnd = lastAppear[s[end]]

            if resChar == s[end] and end == lastAppear[s[end]]:
                res.append(end - start + 1)
                start = end + 1

        return res