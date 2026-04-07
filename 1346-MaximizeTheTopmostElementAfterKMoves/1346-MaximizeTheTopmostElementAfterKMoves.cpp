// Last updated: 07/04/2026, 11:36:46
class Solution {
public:
    int maximumTop(vector<int>& nums, int k) {

        int n = nums.size();
        if ( k ==0 && n!= 0) return nums[0];
        if( n ==1 &&( k%2 ==1)) return -1;
        if ( k ==1) return nums[1];
        
        int  i = 0 ;
        int ans = 0 ; 
        
        if ( k < n){
            ans = nums[k];
            
        }
        --k;


        
        while(k-- && i <n){
            ans = max(ans,nums[i++]);
        }
    
        return ans;
        

        
    }
};