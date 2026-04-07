# Last updated: 07/04/2026, 11:40:56
class Solution:
    def reverseWords(self, s: str) -> str:
        ll = [i for i in s.strip().split()]   
        return " ".join(ll[::-1])
        


        
        