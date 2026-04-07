// Last updated: 07/04/2026, 11:37:57

class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int low = 0; 
        int n = nums.size();
        int high = n -1; 

        while (low <= high ) {

            int mid ; 

            mid = (low+high)/2;

            if (nums[mid]>= target){
                high = mid-1;
            }
            else{
                low = mid +1;
            }

        }

        if ((low <= n-1) && (nums[low] == target)){
            return low ;
        }
        else{
           return  -1;
        }

    }

    };