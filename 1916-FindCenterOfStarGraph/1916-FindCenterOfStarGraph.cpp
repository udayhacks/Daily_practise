// Last updated: 07/04/2026, 11:35:35
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        // Determine the max node index
        int n = 0;
        for (auto &edge : edges)
            n = max({n, edge[0], edge[1]});

        vector<vector<int>> graph(n + 1); // +1 to handle 1-indexed nodes

        for (auto &edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        // The center is the node connected to all others
        for (int i = 1; i <= n; i++) {
            if (graph[i].size() == n - 1) return i;
        }

        return -1;
    }
};
