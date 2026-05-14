class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        brute force is try every triplet with another one

        if two triplets have all max(values) <= target then we can merge them

        """
        curr = [0,0,0]
        for t in triplets:
            max_i = max(t[0], curr[0])
            max_j = max(t[1], curr[1])
            max_k = max(t[2], curr[2])
            if max_i <= target[0] and max_j <= target[1] and max_k <= target[2]:
                curr = [max_i, max_j, max_k]
                if curr == target:
                    return True
        
        return False

