# Last updated: 07/04/2026, 11:42:37
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination(arr,i,target ,ds,ans) :
            if i == len(arr) :
                if target ==0 :
                    ans.append(ds[:])
                    return
                return      
            if arr[i] <= target :
                    ds.append(arr[i])
                    combination(arr,i,target-arr[i],ds,ans)
                    ds.pop()
            combination(arr,i+1,target,ds,ans)
                
                
            return ans
                
        return combination(candidates,0,target,[],[])
                