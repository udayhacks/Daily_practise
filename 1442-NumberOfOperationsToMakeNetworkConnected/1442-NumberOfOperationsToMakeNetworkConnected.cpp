// Last updated: 07/04/2026, 11:36:27
class Solution {
public:
    int findP(int x, vector<int>& parent){
        if (parent[x] != x ){
            return parent[x] = (findP(parent[x],parent));
        }
        return parent[x];
    }
    int makeConnected(int n, vector<vector<int>>& connections) {
        vector<int> parent , rank;
        for(int i = 0 ;i<n;i++){
            parent.push_back(i);
            rank.push_back(0);
        }
        int extra_edges = 0 ;
        int components = 0 ;


        for(auto& cont: connections){
            int a = cont[0];
            int b = cont[1];
            int pa = findP(a,parent);
            int pb = findP(b,parent);
            if (pa == pb){
                extra_edges++;
            }
            else {
                if (rank[pa] == rank[pb]){
                    parent[pa] = pb;
                    rank[pa]++;
                }
                else{
                    if (rank[pa] < rank[pb]){
                        parent[pa] = pb;
                        
                    }else{
                        parent[pb] = pa;
                        
                    }

                }
            }
        }
        for (int i = 0 ; i <n ;i++){
            if (parent[i] ==i ) components++;
        }
        if (extra_edges >= components-1) return components-1;
        return -1;

    }
};