// Last updated: 07/04/2026, 11:40:26
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

    vector<int> rightSideView(TreeNode* root) {
        
        vector<int> ans;
        queue<TreeNode*> q;
        if ( !root) return ans;

        q.push(root);

        while(!(q.empty())){
            int k = q.size();
            int val = -1;
            for( int i = 0;i<k;i++){
                root = q.front();
                if ( i == k-1) ans.push_back(root->val);
                q.pop();
                if ( root->left) q.push(root->left);
                if ( root->right ) q.push(root->right);
            }
            

        }
        return ans;




    }
};