class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def dfs(i, combs):
            if i == len(digits):
                res.append(''.join(combs))
                return

            for char in digitToChar[digits[i]]:
                combs.append(char)
                dfs(i + 1, combs)
                combs.pop()
        

        dfs(0, [])
        return res
