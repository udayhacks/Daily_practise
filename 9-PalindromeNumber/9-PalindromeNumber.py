# Last updated: 07/04/2026, 11:43:49
class Solution(object):
    def isPalindrome(self, x):
        
        k = str(x)
        
        
        
        if x >= 0 and k  == k[::-1]  : return True
        
        return False
        
        