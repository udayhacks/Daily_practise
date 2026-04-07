# Last updated: 07/04/2026, 11:36:13
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root: return 0 # Base case
        cnt = 0 # number of pseudo-palindromic paths
        count = defaultdict(int) # for storing the number of occurences

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal cnt, count
            count[node.val] += 1 # increase the count

            # if we reach the leaf node, check for pseudo-palindromic array
            if not node.left and not node.right:
                odds = 0 # count number of odd occurences
                for key in count:
                    if count[key] % 2:
                        odds += 1
                        if odds > 1: break
                if odds <= 1: cnt += 1 # if it follows all requirements, then we found an answer!
            
            # traverse both subtrees
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            count[node.val] -= 1 # reduce the count, since we are moving backwards to find other paths
        
        dfs(root)
        return cnt