# Last updated: 07/04/2026, 11:38:07
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        
        stack = []

        for i in range(n) :
            
            while stack and stack[-1][0] <temperatures[i] :
                ĵ,l = stack.pop()

                ans[l] = i-l

            stack.append((temperatures[i],i))


        return ans