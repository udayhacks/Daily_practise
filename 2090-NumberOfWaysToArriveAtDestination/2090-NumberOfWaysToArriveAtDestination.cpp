// Last updated: 07/04/2026, 11:35:25
class Solution {

public:
   
int countPaths(int n, vector<vector<int>>& roads) {
    // Creating an adjacency list for the given graph.
    vector<vector<pair<int, int>>> adj(n);
    for (auto it : roads) {
        adj[it[0]].push_back({it[1], it[2]});
        adj[it[1]].push_back({it[0], it[2]});
    }

    // Min-heap priority queue (Dijkstra's Algorithm)
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    // Distance and ways vectors
    vector<long long> dist(n, LLONG_MAX);
    vector<int> ways(n, 0);
    dist[0] = 0;
    ways[0] = 1;
    pq.push({0, 0});

    // Modulo value
    int mod = 1e9 + 7;

    // Dijkstra’s Algorithm
    while (!pq.empty()) {
        long long dis = pq.top().first; // Use long long
        int node = pq.top().second;
        pq.pop();

        for (auto it : adj[node]) {
            int adjNode = it.first;
            int edW = it.second;

            // If a shorter path is found
            if (dis + edW < dist[adjNode]) {
                dist[adjNode] = dis + edW;
                pq.push({dist[adjNode], adjNode});
                ways[adjNode] = ways[node]; // Reset path count
            } 
            // If another shortest path is found, increment count
            else if (dis + edW == dist[adjNode]) {
                ways[adjNode] = (ways[adjNode] + ways[node]) % mod;
            }
        }
    }

    return ways[n - 1] % mod; // Return number of ways to reach node (n-1)
}
    
};