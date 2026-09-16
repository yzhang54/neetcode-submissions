class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # 我看到这个题的时候 第一反应是觉得要用 dp 

        left, right = 0, 0

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                right += 1

            left += 1

        return len(t) - right 