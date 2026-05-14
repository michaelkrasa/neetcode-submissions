class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # how to determine we have a sequence ? n - 1 not in the set = new sequence
        longest = 0
        numSet = set(nums)

        for n in nums:
            if n - 1 not in nums: # start of sequence
                length = 1
                while n + length in nums:
                    length += 1        
                longest = max(longest, length)
        
        return longest
