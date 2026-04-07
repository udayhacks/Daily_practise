# Last updated: 07/04/2026, 11:41:40
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(p,q) :
            if not p and not q :
                return True 
            if p and q :
                if p.val == q.val :
                    if check (p.left, q.left) and check(p.right , q.right) :
                        return True
                return False

          
        return check (p,q)
        