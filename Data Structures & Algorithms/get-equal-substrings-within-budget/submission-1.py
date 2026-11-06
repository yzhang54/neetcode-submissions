class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        left = 0
        curCost = 0
        res = 0
        for right in range(len(s)):
            curCost += abs(ord(s[right]) - ord(t[right]))
            while curCost > maxCost:
                curCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            if curCost <= maxCost:
                res = max(right - left + 1, res)
        
        return res

    
