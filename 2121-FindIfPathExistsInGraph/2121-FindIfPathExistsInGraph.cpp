// Last updated: 07/04/2026, 11:35:23
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool dfs(int node, int destination, vector<vector<int>>& adj, vector<int>& visited) {
        if (node == destination) return true;
        visited[node] = 1;

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, destination, adj, visited)) 
                    return true;
            }
        }
        return false;
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> adj(n);
        vector<int> visited(n, 0);

        // Build adjacency list
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u); // because the graph is undirected
        }

        // Call DFS
        return dfs(source, destination, adj, visited);
    }
};
