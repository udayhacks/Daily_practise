# Last updated: 07/04/2026, 11:36:47
class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0, 1, 1]

        for i in range(3, n+1):
            temp = l[0] + l[1] + l[2]
            l[0] = l[1]
            l[1] = l[2]
            l[2] = temp
        return l[min(n, 2)]