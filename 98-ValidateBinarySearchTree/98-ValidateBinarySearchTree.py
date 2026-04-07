# Last updated: 07/04/2026, 11:41:39
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check (root, mn,mx):
            if root is None :
                return True 
            return root.val > mn and root.val < mx and check(root.left,mn,root.val) and check(root.right,root.val,mx)


        return check(root,float("-inf"),float("inf"))