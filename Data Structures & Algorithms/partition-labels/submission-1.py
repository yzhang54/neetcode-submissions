class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastAppear = defaultdict(int)
        for i in range(len(s)):
            curChar = s[i]
            lastAppear[curChar] = i
        res = []
        start = 0
        resEnd = 0
        for end in range(len(s)):
            resEnd = max(resEnd, lastAppear[s[end]])

            if end == resEnd:
                res.append(end - start + 1)
                start = end + 1

        return res