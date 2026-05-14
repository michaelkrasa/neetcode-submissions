class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Fix window size
        The permutation must be exactly len(s1), so we always use a window of size n = len(s1).
        Build frequency counts
        need[26]: counts for s1.
        have[26]: counts for the current window in s2.
        Index with ord(ch) - ord('a') (only lowercase letters).
        Seed the first window
        Fill have with s2[:n].
        If have == need, we’re done.
        """
        n, m = len(s1), len(s2)
        need = [0] * 26
        have = [0] * 26
        base = ord('a')
        for c in s1:
            need[ord(c) - base] += 1
        for c in s2[:n]:
            have[ord(c) - base] += 1

        if need == have:
            return True

        """
        Slide the window across s2
        For each new index i from n to m-1:
        Add the entering char: s2[i].
        Remove the leaving char: s2[i-n].
        Compare have vs need. If equal → True.
        If no match, return False.
        """
        for i in range(n, m):
            have[ord(s2[i]) - base] += 1
            have[ord(s2[i - n]) - base] -= 1
            if have == need:
                return True
        return False