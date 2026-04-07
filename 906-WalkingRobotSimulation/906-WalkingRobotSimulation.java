// Last updated: 07/04/2026, 11:37:43
import java.util.*;

class Solution {

    public int robotSim(int[] commands, int[][] obstacles) {

        int direction = 0;
        int x = 0;
        int y = 0;

        // Directions: North, East, South, West
        int[][] cal = new int[4][2];
        cal[0] = new int[]{0, 1};
        cal[1] = new int[]{1, 0};
        cal[2] = new int[]{0, -1};
        cal[3] = new int[]{-1, 0};

        // Right turn
        int[] dr = {1, 2, 3, 0};

        // Left turn
        int[] dl = {3, 0, 1, 2};

        int maxdis = 0;

        // Store obstacles in set
        Set<String> obs = new HashSet<>();

        for (int[] o : obstacles) {
            obs.add(o[0] + "," + o[1]);
        }

        for (int cmd : commands) {

            if (cmd > 0) {

                int u = cal[direction][0];
                int v = cal[direction][1];

                while (cmd > 0) {

                    if (!obs.contains((x + u) + "," + (y + v))) {

                        x += u;
                        y += v;

                        maxdis = Math.max(maxdis, x * x + y * y);

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
}