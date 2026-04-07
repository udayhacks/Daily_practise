// Last updated: 07/04/2026, 11:37:33
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
            // here valid num[i,j] = sum ;
            // sum = pref[j] - pref[i-1];
            //here pref[j]- sum = pref[i-1];
            // pref[j] = total sum till now;
            // sum = goal;
            // pref[i-1] = previous cal sum till ith index ; 
            // purely formula shuffling ;

            int total = 0;
            unordered_map<int, int> freq;
            int ans = 0 ;
            freq[0] = 1;

            
            for( int i : nums ){
                total+=i;
                ans+=freq[total-goal];
                freq[total]++;
            }
            return ans;

            

    }
};