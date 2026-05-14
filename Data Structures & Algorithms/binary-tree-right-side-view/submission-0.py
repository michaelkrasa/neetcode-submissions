# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(depth, node):
            if not node:
                return 0
            if depth == len(res):
                res.append(node.val)

            dfs(depth + 1, node.right)
            dfs(depth + 1, node.left)

        dfs(0, root)
        return res