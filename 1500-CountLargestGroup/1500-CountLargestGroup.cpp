// Last updated: 07/04/2026, 11:36:18
class Solution {
int sumOfDigits(int n){
    int s = 0 ;
    int rem= 0 ;
    while (n>0){
        rem = n%10;
        s+=rem;
        n = n/10;
    }
    return s;
}
public:
    int countLargestGroup(int n) {
        unordered_map<int,int> tb ;
        int ans = 0;
        
        for (int i = 1 ;i <=n;i++){
            int k = sumOfDigits(i);
            tb[k]++;
            ans = max(ans,tb[k]);
        }
        int group= 0 ;
        for (auto [k,v]: tb){
            if(v == ans) group++;
        }

    
       return group; 
    }
};