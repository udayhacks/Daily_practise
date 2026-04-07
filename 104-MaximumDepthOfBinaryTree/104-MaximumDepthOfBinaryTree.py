# Last updated: 07/04/2026, 11:41:34
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return  0 

            l = height(root.left)
            r = height (root.right)
            return 1+max(l,r)

        return height(root)

        