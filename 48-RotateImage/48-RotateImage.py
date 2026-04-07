# Last updated: 07/04/2026, 11:42:27
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix[:] = [[matrix[n - 1 - j][i] for j in range(len(matrix))] for i in range(len(matrix))]



        