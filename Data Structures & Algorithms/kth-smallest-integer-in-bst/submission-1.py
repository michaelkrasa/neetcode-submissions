# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # small - left, right
        # dfs - track depth 1-index until k
        # left, node.val, right
        res = None
        cnt = 0

        def inorder(node):
            nonlocal res, cnt
            if not node or res is not None:
                return

            inorder(node.left)

            cnt += 1
            if cnt == k:
                res = node.val
                return

            inorder(node.right)

        inorder(root)
        return res
            