// Last updated: 07/04/2026, 11:37:50
class DisjointSet {
public:
    vector<int> rank, parent, size;

    DisjointSet(int n) {
        rank.resize(n + 1, 0);
        parent.resize(n + 1);
        size.resize(n + 1);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }
    int get_size(int n){
        return size[n];
    }

    int findUPar(int node) {
        if (node == parent[node])
            return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (rank[ulp_u] < rank[ulp_v]) {
            parent[ulp_u] = ulp_v;
        }
        else if (rank[ulp_v] < rank[ulp_u]) {
            parent[ulp_v] = ulp_u;
        }
        else {
            parent[ulp_v] = ulp_u;
            rank[ulp_u]++;
        }
    }
    

    void unionBySize(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (size[ulp_u] < size[ulp_v]) {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};




class Solution {

public:
    bool isvalid(int row,int col,int n){
       return (row<n && col<n && col>= 0 && row>=0); 
    }
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        DisjointSet ds(n*n);
        queue<pair<int,int>> que;
        int dr[] = { -1, 0, 1, 0};
        int dc[] = {0, -1, 0, 1};
           for (int row = 0; row < n ; row++) {
            for (int col = 0; col < n ; col++) {
                if (grid[row][col] == 0) {
                    que.push({row,col});
                    continue;
                    }
                for (int ind = 0; ind < 4; ind++) {
                    int newr = row + dr[ind];
                    int newc = col + dc[ind];
                    if (isvalid(newr, newc, n) && grid[newr][newc] == 1) {
                        int nodeNo = row * n + col;
                        int adjNodeNo = newr * n + newc;
                        ds.unionBySize(nodeNo, adjNodeNo);
                    }
                }
            }
        }
        int island = 0 ;
        while (!que.empty()){
            int row = que.front().first;
            int col = que.front().second;
            que.pop();
            set <int> st;
                for (int ind = 0; ind < 4; ind++) {
                    int newr = row + dr[ind];
                    int newc = col + dc[ind];
                    if (isvalid(newr, newc, n ) && grid[newr][newc] == 1 ) {
                        int adjNodeNo = newr * n + newc;
                        st.insert(ds.findUPar(adjNodeNo));
                }    
        }
         int val = 0 ;
                for (int i : st){
                    val+=(ds.size[i]);
                }
                island = max(island,val+1);
        }



        for (int i = 0 ;i <n*n;i++){
            island = max(island,ds.size[i]);
        }
        return island;
    }
};