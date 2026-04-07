// Last updated: 07/04/2026, 11:43:40
class Solution {
public:
    bool isPalindrome(int x) {
        
        long res = 0;
        int num = x ;
        int rem = 0 ;

        if (x<0){
            return false;
        }


        while (num>0) {

            rem = num%10;
            res = (res*10) +rem;
            num = num/10;

        }

        return res == x;
       

    }
    
};