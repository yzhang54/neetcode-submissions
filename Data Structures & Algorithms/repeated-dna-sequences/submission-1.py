class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
        left = 0
        for right in range(10, len(s)+1):
            while right - left > 10:
                left += 1

            # print("seen", seen)
            # print(s[left:right])
            if s[left:right] in seen:
                res.add(s[left:right])
            seen.add(s[left:right])

        return list(res)