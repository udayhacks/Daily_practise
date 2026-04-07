// Last updated: 07/04/2026, 11:41:17
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res = root->val;
        dfs(root,res);
        return res;
    }
private:
    int dfs(TreeNode* node, int& res){
        if ( !node){ return 0 ; }
        int left_s = max(0,dfs(node->left, res));
        int right_s = max(0, dfs(node->right,res));
        res = max( res, left_s+right_s+node->val);
        return max(left_s,right_s)+node->val;
    }
};