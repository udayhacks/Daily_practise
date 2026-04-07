# Last updated: 07/04/2026, 11:38:40
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(node: TreeNode):
            if node.left:
                inorder(node.left)
            node_values.append(node.val)
            if node.right:
                inorder(node.right)
        
        node_values = []

        inorder(root)

        return min(node_values[i+1] - node_values[i] for i in range(len(node_values)-1))



          






        