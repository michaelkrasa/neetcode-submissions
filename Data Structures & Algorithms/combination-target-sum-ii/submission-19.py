class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            
            while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
    
