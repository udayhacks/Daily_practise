# Last updated: 07/04/2026, 11:41:37
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None :
            return []
        ans = []
        que = [root]

        while que :
            k = len(que)
            s = []
            for i in range(k):
                j = que.pop(0)
                s.append(j.val)
                if j.left :
                    que.append(j.left)
                if j.right :
                    que .append(j.right)

            ans.append(s)

        return ans
   
