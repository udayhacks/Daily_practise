# Last updated: 07/04/2026, 11:38:16
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s)-1

        while i < j :
            if s[i] != s[j] :
                k = s[:i]+s[i+1:]
                l = s[:j]+s[j+1:]

                if k == k[::-1]:
                    return True
                elif l == l[::-1]:
                    return True 
            
                else:
                    return False

            i+=1
            j-=1
            


        return True
                
