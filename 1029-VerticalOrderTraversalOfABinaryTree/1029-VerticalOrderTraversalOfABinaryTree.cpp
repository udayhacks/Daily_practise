// Last updated: 07/04/2026, 11:37:20
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
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        
        map<int,vector<pair<int,int>>> mp;
        // col = {{row1,val1},.........}
        vector<vector<int>> ans;
        // stores answeres

        queue<tuple<int ,int ,TreeNode*>> q;

        q.push({0,0,root});
        
        while(!(q.empty())){
            
            auto [col ,row , node] = q.front();
            q.pop();
            mp[col].push_back({row,node->val});
            if ( node->left) q.push({col-1,row+1,node->left});
            if ( node->right) q.push({col+1,row+1,node->right});
            
        }
        for ( auto [col, nodes]:mp){
            sort(nodes.begin(),nodes.end());
            vector<int> tmp;
            for ( auto [row,val] : nodes){
                tmp.push_back(val);
            }
            ans.push_back(tmp);
        }
        return ans;





    }
};