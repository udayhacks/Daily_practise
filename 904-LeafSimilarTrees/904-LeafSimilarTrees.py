# Last updated: 07/04/2026, 11:37:42
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leav (root,res = []) :
            if root :
                if root.left is None and root.right is None :
                    res.append(root.val)
                    return res 
                
                leav(root.left ,res)
                leav(root.right,res)

                return res


            



        k = leav(root1,[])
        h = leav(root2,[])
        return k == h
        

                
                

      

        
                
        
       
        