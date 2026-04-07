// Last updated: 07/04/2026, 11:41:45
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
    void Traversal(TreeNode* root,vector <int> &arr) {
        if (root){
            
            Traversal(root->left,arr);
            arr.push_back(root->val);
            Traversal(root->right,arr);

            }
        }
    vector<int> inorderTraversal(TreeNode* root) {
        vector <int> arr;
        Traversal(root,arr);
        return arr;
    }
};