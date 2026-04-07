# Last updated: 07/04/2026, 11:41:31
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checker(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (node1.val == node2.val and checker(node1.left, node2.right) and checker(node1.right, node2.left))
            
        return checker(root.left, root.right)

        return check (root)

       
