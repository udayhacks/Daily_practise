// Last updated: 07/04/2026, 11:38:06
class Solution {
private:
    vector<int> dijkstra(vector<vector<pair<int, int>>>& adj, int src) {
        int V = adj.size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> dist(V, 1e9);

        dist[src] = 0;
        pq.push({0, src});

        while (!pq.empty()) {
            int node = pq.top().second;
            int node_dist = pq.top().first;
            pq.pop();

            for (auto& i : adj[node]) {
                int adjNode = i.first;
                int weight = i.second;
                if (node_dist + weight < dist[adjNode]) {
                    dist[adjNode] = node_dist + weight;
                    pq.push({dist[adjNode], adjNode});
                }
            }
        }
        return dist;
    }

public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> adj(n);

       
        for (int i = 0; i < times.size(); i++) {
            int src = times[i][0] - 1; // Convert to 0-based
            int dst = times[i][1] - 1; // Convert to 0-based
            int time = times[i][2];

            adj[src].push_back({dst, time});
        }

        
        vector<int> vec = dijkstra(adj, k - 1);

       int mx = vec[0];
       for(int i :vec){
        if (i == 1e9) return -1 ; 
        if (i>mx) mx = i ;
       }
       return mx;
       
    }
};