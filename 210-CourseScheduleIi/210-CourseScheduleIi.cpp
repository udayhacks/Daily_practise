// Last updated: 07/04/2026, 11:40:16
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {

        vector<int>ans;
        int n = numCourses;
        vector<int> indegree(n);
        vector<vector<int>> adj(n);
        for ( auto & pre : prerequisites){

            int a = pre[0];
            int b = pre[1];
            adj[b].push_back(a);
            indegree[a]++;


        }
        queue<int> q;
        for ( int i = 0; i<n;i++){
            if ( indegree[i]== 0) q .push(i);
        }

        while(!q.empty()){
            int node = q.front();
            q.pop();
            ans.push_back(node);
            for( int i : adj[node]){
                indegree[i]--;
                if ( indegree[i]== 0) q.push(i);
            }
        }

        if ( n != (int)ans.size()) return { };
        else return ans; 


        
        
    }
};