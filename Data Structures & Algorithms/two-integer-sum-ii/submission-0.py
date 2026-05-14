class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        0, 1, 1, 2..
        two pointers
        decrement j while bigger than target
        check n[i] whether they add up to target
        while bigger decrement j
        while smaller increment i

        return i j
        """

        i, j = 0, len(numbers) - 1

        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            if s < target:
                i += 1
            else:
                j -= 1
            
        return []
        