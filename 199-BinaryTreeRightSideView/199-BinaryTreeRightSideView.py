# Last updated: 07/04/2026, 11:40:31
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        qu, res =[], []
        qu.append(root)
        while len(qu)>0:
            lgt = len(qu)
            for i in range(lgt):
                node=qu.pop(0)
                if i==lgt-1:
                    res.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
        return res



        
        