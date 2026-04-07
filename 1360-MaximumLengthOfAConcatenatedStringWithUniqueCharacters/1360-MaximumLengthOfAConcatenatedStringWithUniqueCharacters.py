# Last updated: 07/04/2026, 11:36:38
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def solve(curr_str, ind, mapp):
            if mapp and max([i for i in mapp.values()])>1:
                return
            if ind>=len(arr):
                res[0] = max(res[0], len(curr_str))
                return
            for i in arr[ind]:
                mapp[i] = mapp.get(i, 0)+1
            
            solve(curr_str + arr[ind],ind+1,mapp)
            for i in arr[ind]:
                mapp[i] -= 1
            solve(curr_str, ind+1, mapp)
        solve("",0,{})
        return res[0]