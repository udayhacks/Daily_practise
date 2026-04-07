# Last updated: 07/04/2026, 11:35:45
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c = 0
        l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        k = len(s) 
        for i  in range(k//2) :
            if s[i] in l :
                c+=1

        for j in range(i+1,k):
            if s[j] in l :
                c-=1



        if c == 0 :
            return True 
        return False

    

            
        

        