class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
        left = 0
        for right in range(9, len(s)):
            while right - left + 1 > 10:
                left += 1

            # print("seen", seen)
            # print(s[left:right])
            if s[left:right+1] in seen:
                res.add(s[left:right+1])
            seen.add(s[left:right+1])

        return list(res)