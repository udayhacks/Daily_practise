# Last updated: 07/04/2026, 11:36:03
class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        m = 0 
        for i in s :
            if  i == "(" :
                st.append(i) 
            elif i == ")":
                st.pop()
            m = max(len(st),m)

        return m
        