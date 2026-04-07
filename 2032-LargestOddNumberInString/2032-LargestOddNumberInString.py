# Last updated: 07/04/2026, 11:35:36
class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = [1,3,5,7,9]
        j = len(num)-1
        while j >= 0 :
            if int(num[j])%2 == 1 :
                return num[:j+1]
            j-=1
    

        return ""
        