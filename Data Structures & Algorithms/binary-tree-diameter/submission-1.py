class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter
            if not node:
                return 0

            height_l = height(node.left)
            height_r = height(node.right)

            # max length of both trees that pass through this node
            diameter = max(diameter, height_l + height_r)
            return 1 + max(height_l, height_r)

        height(root)
        return diameter