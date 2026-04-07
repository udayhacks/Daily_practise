// Last updated: 07/04/2026, 11:37:52
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        
    
        vector< vector< pair<int,int>>> adj(n) ;

        for(auto i :flights){
            adj[i[0]].push_back({i[1],i[2]});
        }

        queue<pair<int,pair<int,int>>>que;
        vector<int> prices(n,1e9);

        prices[src] = 0;

        que.push({0,{src,prices[src]}});

        while (!que.empty()){
            auto top = que.front();
            int stop  = top.first;
            int node = top.second.first;
            int dis = top.second.second;
            que.pop();


            for(auto& it :adj[node]){
                int adjnode = it.first;
                int wt = it.second;

                if (dis+wt<prices[adjnode] && stop <= k ){
                    prices[adjnode] = dis+wt;
                    que.push({stop+1,{adjnode,dis+wt}});
                }
            }
        }
        if (prices[dst] == 1e9) return -1;
        return prices[dst];




            

        }
        
    
};