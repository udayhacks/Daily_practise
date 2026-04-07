// Last updated: 07/04/2026, 11:38:01
class Solution {
public:


    int maxChunksToSorted(vector<int>& arr) {
        int maxvalue = 0 ;
        int maxp = 0 ;

        for (int i = 0 ; i < arr.size(); i++) {

            if (maxvalue < arr[i] ) {
                maxvalue = arr[i];
            }
            if (i== maxvalue) {
                ++maxp;

            }
        }


    return maxp;

    }
};