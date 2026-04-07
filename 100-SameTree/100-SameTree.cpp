// Last updated: 07/04/2026, 11:41:36
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
    bool check(TreeNode* p, TreeNode * q){
        if ( p == nullptr && q == nullptr)return true;

        if ( p && q){
            if ( p->val == q->val){
                if ( check(p->left,q->left) && check(p->right, q->right)) return true;
                return false;
            }
        }
        return false;
        
     



}   
    bool isSameTree(TreeNode* p, TreeNode* q) {
        
       return check(p,q);
    }
};