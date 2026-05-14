class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # combination sum - no sorting
        combinations = []

        def dfs(i, combs, curSum):
            if curSum == target:
                combinations.append(combs.copy())
                return

            if i == len(nums) or curSum > target:
                return

            # choose
            combs.append(nums[i])
            dfs(i, combs, curSum + nums[i])

            # next
            combs.pop()
            dfs(i + 1, combs, curSum)
            
        dfs(0, [], 0)

        return combinations