// Last updated: 07/04/2026, 11:42:06
class Solution {

    private:
 
    int arr[10000];

    int F(int n){
        if ( n == 1) return 1; 
        if ( n == 2) return 2;
        if (arr[n] != -1 ) return arr[n];
        return  arr[n] = F(n-1)+F(n-2);
    }

    public:
        int climbStairs(int n) {
            memset(arr,-1,size(arr));

            //base 
            arr[1] = 1;
            arr[2] = 2;
            for ( int i = 3 ;i<=n;i++){
                arr[i] = arr[i-1]+arr[i-2];
            }return arr[n];
            
        return F(n); 
        }

};