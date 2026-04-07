// Last updated: 07/04/2026, 11:39:32
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        vector<int> degree(n);
        vector<vector<int>> adj(n);
        if ( n ==1) return {0};
      for (auto &e : edges) {
    int u = e[0];
    int v = e[1];
    adj[u].push_back(v);
    adj[v].push_back(u);
    degree[u]++;
    degree[v]++;
}


        queue<int> q;
        for ( int i = 0;i<n;i++){
            if ( degree[i] ==1) q.push(i);
        }
        int rem = n;
        while(rem>2){
            int qs = q.size();
            rem -= qs;
            for( int i = 0;i<qs;i++){
                int node = q.front();
                q.pop();
                for ( int an : adj[node]){
                   degree[an]--;
                   if ( degree[an] ==1 ) q.push(an); 
                }
            }
        }
        vector<int> result;
        while(!q.empty()){
            int i = q.front();q.pop();
            result.push_back(i);
        }
        return result;

        
    }
};