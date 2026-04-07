# Last updated: 07/04/2026, 11:41:01
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tras(self,root,ans):
        if root :
            ans.append(root.val)
            self.tras(root.left,ans)
            self.tras(root.right,ans)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.tras(root,ans)
        return ans
        