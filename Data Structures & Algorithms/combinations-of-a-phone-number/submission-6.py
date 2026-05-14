class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
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

        res, path = [], []
        def dfs(i):
            if i == len(digits):
                res.append(''.join(path))
                return

            for ch in digitToChar[digits[i]]:
                path.append(ch)
                dfs(i + 1)
                path.pop()

        if digits:
            dfs(0)
        
        return res