// Last updated: 07/04/2026, 11:37:48
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {

        int direction = 0;
        int x = 0;
        int y = 0;

        // Directions: North, East, South, West
        vector<pair<int,int>> cal(4);
        cal[0] = {0,1};
        cal[1] = {1,0};
        cal[2] = {0,-1};
        cal[3] = {-1,0};

        // Right turn
        vector<int> dr = {1,2,3,0};

        // Left turn
        vector<int> dl = {3,0,1,2};

        int maxdis = 0;

        // Store obstacles in set
        set<pair<int,int>> obs;
        for (auto &o : obstacles) {
            obs.insert({o[0], o[1]});
        }

        for (int cmd : commands) {

            if (cmd > 0) {

                auto [u,v] = cal[direction];

                while (cmd > 0) {

                    if (obs.find({x+u, y+v}) == obs.end()) {

                        x += u;
                        y += v;

                        maxdis = max(maxdis, x*x + y*y);

                    } else {
                        break;
                    }

                    cmd--;
                }

            } 
            else if (cmd == -1) {
                direction = dr[direction];
            } 
            else if (cmd == -2) {
                direction = dl[direction];
            }
        }

        return maxdis;
    }
};