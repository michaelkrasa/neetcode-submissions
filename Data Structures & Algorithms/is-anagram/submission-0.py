class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # use a map, k:letter v:char count
        # scan first string and store in map
        m = {}
        n = {}

        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1

        for c in t:
            if c not in n:
                n[c] = 1
            else:
                n[c] += 1

        if len(n) != len(m):
            return False

        for k, v in m.items():
            if k not in n or v != n[k]:
                return False

        return True



        