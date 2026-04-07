// Last updated: 07/04/2026, 11:38:55
class Solution {
public:
    string frequencySort(string s) {
        map<char,int> freq;


        for ( char c : s) freq[c]++;
        priority_queue<pair<int,char>> pq;
        for ( auto[c,i]: freq){
            pq.push({i,c});
        }
        string ans;
        
        while(!pq.empty()){
            auto [i,c] = pq.top();
            while(i--) ans+=c;
            pq.pop();
        }return ans;

    }
};