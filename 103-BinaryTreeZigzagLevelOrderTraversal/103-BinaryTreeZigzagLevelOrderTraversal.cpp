// Last updated: 07/04/2026, 11:41:30
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        
        vector<vector<int>> ans;
        queue<TreeNode *> st;
        if ( root==nullptr) return ans;

        st.push(root);
        
        int m = -1;
        
        while(!(st.empty())){
            
            m++;
            int k = st.size();
            vector<int> temp;

            for ( int i = 0;i<k;i++){
                
                root = st.front();
                st.pop();
                temp.push_back(root->val);
                if (root->left) st.push(root->left);
                if (root->right) st.push(root->right);
 
            }

            if ( m%2 ==1){
                reverse(temp.begin(),temp.end());
            }
            ans.push_back(temp);

            
        }
        return ans;







    }
};