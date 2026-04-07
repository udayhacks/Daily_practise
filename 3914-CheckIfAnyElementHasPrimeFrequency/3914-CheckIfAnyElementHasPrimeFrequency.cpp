// Last updated: 07/04/2026, 11:33:36
class Solution {
public:
    bool checkPrimeFrequency(vector<int>& nums) {
        vector<int> prime {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97
            };


    vector<int> primef(101,0);
        for (int i =0;i<prime.size();i++){
            primef[prime[i]] = 1;
        }
         unordered_map<int,int> freq;
        for (int i = 0 ;i <nums.size();i++){
            freq[nums[i]]++;
        }
        for(auto &i : freq){
            if (primef[i.second ] == 1 ) return true;
                
        }
        return false;
        
    }
};