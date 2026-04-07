// Last updated: 07/04/2026, 11:35:30

class Solution {
public:
    int minCost(int maxTime, vector<vector<int>>& edges, vector<int>& passingFee) {
        int n = passingFee.size();
        vector<vector<pair<int, int>>> adj(n);

        for (auto &e : edges) {
            int u = e[0], v = e[1], t = e[2];
            adj[u].push_back({v, t});
            adj[v].push_back({u, t});
        }

        // cost[node][time] = min cost to reach node at given time
        vector<int> cost(n, INT_MAX);
        vector<int> time(n, INT_MAX);

        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        pq.push({passingFee[0], 0, 0}); // {cost, time, node}
        cost[0] = passingFee[0];
        time[0] = 0;

        while (!pq.empty()) {
            auto cur = pq.top(); pq.pop();
            int c = cur[0], t = cur[1], u = cur[2];

            if (u == n - 1) return c;

            for (auto &[v, w] : adj[u]) {
                int newTime = t + w;
                int newCost = c + passingFee[v];

                if (newTime <= maxTime && (newCost < cost[v] || newTime < time[v])) {
                    cost[v] = min(cost[v], newCost);
                    time[v] = min(time[v], newTime);
                    pq.push({newCost, newTime, v});
                }
            }
        }

        return -1;
    }
};
