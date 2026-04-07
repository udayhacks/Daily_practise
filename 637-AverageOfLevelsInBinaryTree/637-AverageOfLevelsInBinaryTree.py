# Last updated: 07/04/2026, 11:38:24
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]: 

        ans = []
        que = [root]

        while que :
            k = len(que)
            s = 0
            for i in range(k):
                j = que.pop(0)
                s+=j.val
                if j.left :
                    que.append(j.left)
                if j.right :
                    que .append(j.right)

            ans.append(s/k)

        return ans


