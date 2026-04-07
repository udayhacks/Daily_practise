# Last updated: 07/04/2026, 11:36:22
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        def countNegativesInRows(row):
            left = 0
            right = len(row) -1
            while left <= right:
                mid = math.ceil(left + right) // 2
                if row[mid] < 0:
                    right = mid -1
                else:
                    left = mid + 1
            return len(row) - (right + 1)

        for i in range(len(grid)):
            count += countNegativesInRows(grid[i])
        return count 
        