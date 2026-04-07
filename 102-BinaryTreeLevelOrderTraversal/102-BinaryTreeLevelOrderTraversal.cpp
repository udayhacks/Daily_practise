// Last updated: 07/04/2026, 11:41:32
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == nullptr) return {};
        queue<TreeNode *> stack;
        stack.push(root);
        while(stack.size()){
            vector <int> s;
            int j = stack.size();
            
            for (int i = 0 ;i<j;i++){
                TreeNode *k = stack.front();
                stack.pop();
                s.push_back(k->val);
                if (k->left != nullptr){
                stack.push(k->left);
                }
                if (k->right != nullptr){
                stack.push(k->right);
                }
            }
            ans.push_back(s);
            
        
        }
        return ans;



    }
};