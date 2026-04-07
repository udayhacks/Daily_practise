// Last updated: 07/04/2026, 11:38:36
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
    int diameter(TreeNode *root,int &d){
        if( root == nullptr) return 0;
        int left = diameter(root->left,d);
        int right = diameter(root->right,d);
        d = max(left+right,d);
        return 1+max(left,right);

    }
    int diameterOfBinaryTree(TreeNode* root) {
        int d = 0;
        diameter(root,d);
        return d;
    }
};