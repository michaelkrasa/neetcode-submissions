class Solution:
    def isValid(self, s: str) -> bool:
        """
        push, pop, peek
        () [] {}
    
        loop through the string
        if beginning bracket then we push it onto the stack
        if ending bracket we peek the top, 
            if it is the correct opposite we pop it
        else
            return false

        return
        

        ([{}])
        ([{)
        """


        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in pairs.values():       # opening
                stack.append(c)
            else:                          # closing
                if not stack or stack[-1] != pairs.get(c, None):
                    return False
                stack.pop()
        return not stack


