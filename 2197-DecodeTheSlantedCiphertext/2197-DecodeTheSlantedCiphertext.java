// Last updated: 07/04/2026, 11:35:17
class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        
        int n = encodedText.length();
        if (n == 0) return "";
        
        int cols = n / rows;

        // Step 1: Fill matrix
        char[][] M = new char[rows][cols];
        int k = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                M[r][c] = encodedText.charAt(k++);
            }
        }

        // Step 2: Traverse diagonally
        StringBuilder ans = new StringBuilder();

        for (int c = 0; c < cols; c++) {
            int r = 0;
            int col = c;

            while (r < rows && col < cols) {
                ans.append(M[r++][col++]);
            }
        }

        // Step 3: Remove trailing spaces
        int end = ans.length() - 1;
        while (end >= 0 && ans.charAt(end) == ' ') {
            end--;
        }

        return ans.substring(0, end + 1);
    }
}