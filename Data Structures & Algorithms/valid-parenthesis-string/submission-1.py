class Solution:
    def checkValidString(self, s: str) -> bool:
        opening = closing = star = 0
        left = []
        star = []
        """
        "((**)"

        "(((*)"

        we can use stacks and compare indices of star and left
        """

        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False

        return not left

        

                
                


