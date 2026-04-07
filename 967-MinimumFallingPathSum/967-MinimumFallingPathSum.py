# Last updated: 07/04/2026, 11:37:32
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        val = int(1e9)
        dp = [-1] * n

        for j in range(n):
            dp[j] = matrix[0][j]

        for i in range(1, n):
            tmp = [0] * n
            for j in range(n):
                dia = int(1e9)
                dia2 = int(1e9)
                str_val = matrix[i][j] + dp[j]
                if j + 1 < n:
                    dia = matrix[i][j] + dp[j + 1]
                if j - 1 >= 0:
                    dia2 = matrix[i][j] + dp[j - 1]
                tmp[j] = min(min(dia, dia2), str_val)
            dp = tmp

        for i in range(n):
            val = min(dp[i], val)

        return val
            