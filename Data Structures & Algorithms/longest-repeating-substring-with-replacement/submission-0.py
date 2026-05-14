class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        use a map, iterate and get num of unique characters .. and their counts?

        """
        res = l = maxf = 0
        chars = {}

        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            maxf = max(maxf, chars[s[r]])

            while r - l + 1 - maxf > k:
                chars[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res