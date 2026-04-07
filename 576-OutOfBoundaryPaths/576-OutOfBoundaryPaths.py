# Last updated: 07/04/2026, 11:38:32
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(i, j, moves):
            if moves < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            res = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                res += dfs(i + dx, j + dy, moves - 1)
            return res % (10**9 + 7)

        return dfs(startRow, startColumn, maxMove)
