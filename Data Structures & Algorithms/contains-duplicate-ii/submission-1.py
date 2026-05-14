class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # contains duplicate within range of each other
        dup = set()
        L = 0

        for R in range(len(nums)):
            # window too long
            if R - L > k:
                dup.remove(nums[L])
                L += 1
            if nums[R] in dup:
                return True
            dup.add(nums[R])
        
        return False
        