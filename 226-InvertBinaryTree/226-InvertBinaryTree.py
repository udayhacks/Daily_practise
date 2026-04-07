# Last updated: 07/04/2026, 11:40:05
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        rootRight = root.right

        root.right = root.left
        root.left = rootRight

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        