# Last updated: 07/04/2026, 11:35:55
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = -1 
        points.sort(key = lambda x :x[0])

        for i in range(1, len(points)) :
            ans = points[i][0] -points[i-1][0]
            res = max(res,ans)


        return res 
        