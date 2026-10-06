class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counter = Counter(s)
        res = ""
        for i in range(len(order)):
            if order[i] in counter:
                res += order[i] * counter[order[i]]

        orderSet = set(order)
        for char in s:
            if char not in orderSet:
                res += char

        return res

        