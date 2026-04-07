// Last updated: 07/04/2026, 11:41:53
class Solution {
public:

    void func(vector<vector<int>> & ans , vector <int> &path, vector<int> &nums,int i )   {

        if (i == nums.size()) {
            ans.push_back(path);
            return ;    
        }

        path.push_back(nums[i]);
        func(ans,path,nums,i+1);
        path.pop_back();
        func(ans,path,nums,i+1);


    }

    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector <vector <int>> ans ;
        vector <int> path;
        int i = 0 ;
        func(ans,path,nums,i);
        return ans;



    }
};