// Last updated: 07/04/2026, 11:42:16
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {

        vector<vector<int>> ans;
        intervals.push_back(newInterval);
        sort(intervals.begin(),intervals.end());

        ans.push_back(intervals[0]);
        int n = intervals.size();
        for ( int i = 1 ;i<n;i++){

            auto &last = ans.back();
            auto &interval = intervals[i];

            if ( last[0] <=interval[0] &&  last[1] >= interval[0]  ){
                last[0] = min(last[0],interval[0]);
                last[1] = max(last[1],interval[1]);
            }
            else{
                ans.push_back(interval);
            }
        }
        return ans;
        
    }
};