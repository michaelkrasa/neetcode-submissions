class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # how to determine we have a sequence ? n - 1 not in the set = new sequence
        """
        add to a set
        check if n-1 present, if not start new sequence
        if it is sequence += 1
        """

        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in nums:
                length = 0
                while n + length in nums:
                    length += 1
                
                longest = max(longest, length)

        return longest
