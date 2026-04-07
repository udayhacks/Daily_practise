// Last updated: 07/04/2026, 11:40:19
class Solution {
public:
   bool isCyclic(vector<vector<int>> &adj) {
        
        int v = adj.size();
        vector<int> arr(v,0);
        
        for (int i = 0 ; i<v; i++){
            for (int j : adj[i]){
                arr[j]++;
            }
        }
        
        int cnt = 0 ; 
        queue<int> que;
        
        for (int i = 0 ; i<v;i++){
            if (arr[i] == 0 ) que.push(i);
        }
        
        while (!que.empty()){
            int front = que.front();
            cnt ++;
            que.pop();
            for (int i :adj[front]){
                arr[i]--;
                if (!arr[i]) que.push(i);
            }
        }
        
        
        if (cnt == v ) return 1;
        return 0;
        
        
        
    
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for (auto i:prerequisites){
            adj[i[1]].push_back(i[0]);
        }

        return isCyclic(adj);








    }
};