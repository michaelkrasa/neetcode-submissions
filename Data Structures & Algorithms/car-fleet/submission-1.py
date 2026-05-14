class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        fast cars catch up to the faster ones
        we can use a stack to keep track of which cars ahead are faster

        """

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        # s / (v * t)

        for s, v in pair:
            time = (target - s) / v
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)