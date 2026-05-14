class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        is_anagram() --> using sets
        
        dict of anagrams

        k: anagram set v: list (append)

        """
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            groups[key].append(s)
        return list(groups.values())