class Solution:
    def permute(self, nums):
        self.res = []
        print(f"\nSTART permute({nums})")
        self.backtrack(nums, 0)
        print("\nDONE\n")
        return self.res

    def backtrack(self, nums, idx):
        print(f"{'  ' * idx}--> backtrack(idx={idx}, nums={nums})")

        # BASE CASE
        if idx == len(nums):
            print(f"{'  ' * idx}*** BASE CASE HIT: append {nums} ***")
            self.res.append(nums.copy())
            return

        # TRY ALL SWAPS
        for i in range(idx, len(nums)):
            print(f"{'  ' * idx}Swap idx={idx} with i={i}: {nums[idx]} <-> {nums[i]}")
            nums[idx], nums[i] = nums[i], nums[idx]

            print(f"{'  ' * idx}After swap: {nums}")
            print(f"{'  ' * idx}Recurse into idx={idx+1}")

            self.backtrack(nums, idx + 1)

            print(f"{'  ' * idx}Backtrack: undo swap idx={idx} with i={i}")
            nums[idx], nums[i] = nums[i], nums[idx]
            print(f"{'  ' * idx}After undo: {nums}")
