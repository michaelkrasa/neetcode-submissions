class Solution:
    def checkValidString(self, s: str) -> bool:
        
        bal = 0
        for ch in s:
            if ch in '(*': 
                bal += 1
            else:
                bal -= 1
            if bal < 0:    # too many ')'
                return False

        # right-to-left: treat * as ')'
        bal = 0
        for ch in reversed(s):
            if ch in ')*':
                bal += 1
            else:         
                bal -= 1
            if bal < 0:    # too many '('
                return False

        return True