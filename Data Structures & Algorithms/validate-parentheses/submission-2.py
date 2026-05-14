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
        """

        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
                continue
            
            if not stack:
                return False

            top = stack[-1]
            if (top == '(' and c != ')') or (top == '[' and c != ']') or (top == '{' and c != '}'):
                return False
            else:
                stack.pop()

        return len(stack) == 0
