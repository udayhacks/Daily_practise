# Last updated: 07/04/2026, 11:42:52
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      
        if needle in haystack :
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1




        



        
        