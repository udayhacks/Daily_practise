# Last updated: 07/04/2026, 11:40:01
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 1
        self.ans = None
        
        def small(root):
            
            if root is None  or self.ans :
                return 
            aa= root.val
            small(root.left)
            if self.counter == k :
                self.ans = root.val 
            self.counter+=1
            small(root.right)
            
        small(root)
        return self.ans
                
                 
        