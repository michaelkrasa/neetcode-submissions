class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        # appending to subsets
        # dfs [], [1], [1,2]

        def dfs(i, curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            # 2 choices - append or ignore
            curSet.append(nums[i])
            dfs(i + 1, curSet)

            curSet.pop()
            dfs(i + 1, curSet)

        dfs(0, [])

        return subsets