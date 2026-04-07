# Last updated: 07/04/2026, 11:38:04
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0 
        h= len(letters)-1
        while l <= h :
            m = (l+h)//2
            if letters[m] <=target :
                l= m+1
            else:
                h = m-1
        return letters[l] if  l< len(letters)  else  letters[0]

            
           

        