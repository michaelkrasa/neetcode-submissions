class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        is_anagram() --> using sets
        
        dict of anagrams

        k: anagram set v: list (append)

        """
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                char_i = ord(c) - ord('a')
                count[char_i] += 1
            res[tuple(count)].append(s)

        return list(res.values())