class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        iterate until we hit one of the signs
        use a stack? 
        whenever we encounter a symbol we evaluate the expression
        and continue with the iteration
        """
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(t))
        return stack.pop()

        