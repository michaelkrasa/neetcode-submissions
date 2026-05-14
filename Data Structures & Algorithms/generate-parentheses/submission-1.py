class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        ( -> (), ((
        ) -> x

        () -> ()(
        (( -> (((, (()

        ((( -> ((()))

        (()(
    
        open p
        closed p

        open == closed == n

        open < n
        closed < open
        """
        res = []
        def backtrack(curr: str, open_used: int, close_used: int) -> None:
            # If the string is complete, record it
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # We can add "(" if we still have some left to place
            if open_used < n:
                backtrack(curr + "(", open_used + 1, close_used)

            # We can add ")" only if it won't make the prefix invalid
            if close_used < open_used:
                backtrack(curr + ")", open_used, close_used + 1)

        backtrack("", 0, 0)
        return res