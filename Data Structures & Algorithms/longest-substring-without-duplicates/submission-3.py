class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        have a hashset, move right pointer until we have a colission
        save max hashset length
        remove s[l]++ while s[r] in hashset
        xyzxyz
        """
        l = 0
        chars = set()
        maxLen = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen
                
                

        return maxLen
        