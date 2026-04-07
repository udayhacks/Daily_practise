// Last updated: 07/04/2026, 11:42:39
class Solution {
private:

    bool isSafe(vector<vector<char>>& board, int row, int col, char dig) {
        
        // column check
        for (int r = 0; r < 9; r++) {
            if (board[r][col] == dig) return false;
        }

        // row check
        for (int c = 0; c < 9; c++) {
            if (board[row][c] == dig) return false;
        }

        // 3x3 box check
        int sr = (row / 3) * 3;
        int sc = (col / 3) * 3;

        for (int r = sr; r < sr + 3; r++) {
            for (int c = sc; c < sc + 3; c++) {
                if (board[r][c] == dig) return false;
            }
        }

        return true;
    }

    bool helper(vector<vector<char>>& board, int row, int col) {
        
        if (row == 9) return true;

        int next_row = row;
        int next_col = col + 1;

        if (next_col == 9) {
            next_row = row + 1;
            next_col = 0;
        }

        if (board[row][col] != '.') {
            return helper(board, next_row, next_col);
        }

        for (char dig = '1'; dig <= '9'; dig++) {
            if (isSafe(board, row, col, dig)) {
                board[row][col] = dig;

                if (helper(board, next_row, next_col)) return true;

                board[row][col] = '.';
            }
        }

        return false;
    }

public:

    void solveSudoku(vector<vector<char>>& board) {
        helper(board, 0, 0);
    }
};