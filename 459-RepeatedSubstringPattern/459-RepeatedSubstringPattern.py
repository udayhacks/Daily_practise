# Last updated: 07/04/2026, 11:38:49
class Solution:
       def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]