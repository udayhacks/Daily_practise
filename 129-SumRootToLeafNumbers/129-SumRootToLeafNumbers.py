# Last updated: 07/04/2026, 11:41:10
class Solution:
    def sumNumbers(self, root) -> int:

        ans = [0]

        def tree_traversal(root, curr, ans):
            k = root.val
            curr += str(k)

            if root.left == None and root.right == None:
                ans[0] = ans[0] + int(curr)
                return

            if root.left:
                tree_traversal(root.left, curr, ans)
            
            if root.right:
                tree_traversal(root.right, curr, ans)
        
        tree_traversal(root, '', ans)
        return ans[0] 
    
    
    