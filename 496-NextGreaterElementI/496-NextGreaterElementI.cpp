// Last updated: 07/04/2026, 11:38:46
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> list;
        stack<int> stck;
        vector<int>ans ;

        for(int &i : nums2){
            while (!stck.empty() && stck.top()<i){
                list[stck.top()] = i;
                stck.pop();
            }
            stck.push(i);
        }
        while(!stck.empty()){
           list[stck.top()] = -1;
           stck.pop(); 
        }
        for(int &i: nums1){
           ans.push_back(list[i]); 
        }
        return ans;
    }

};