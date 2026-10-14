class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # track the max freq and the letter 
        # track the rest of freq and letter 

        window = defaultdict(int) # letter: int
        left = 0
        res = 0
        for right in range(len(s)):
            curLetter = s[right]
            window[curLetter] += 1

            maxpair = [0, ""]
            for letter, freq in window.items():
                if freq > maxpair[0]:
                    maxpair = [freq, letter]

            while maxpair[0] + k < right - left + 1:
                window[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)


        return res
            





