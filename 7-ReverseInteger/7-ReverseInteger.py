# Last updated: 07/04/2026, 11:43:51
class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 -1
        min_int = -2**31 
        rev = 0 
        while x != 0 :
            if rev > max_int/10 or rev < min_int/10 :
                return 0 
            dig = x % 10 if x > 0 else x %-10
            rev = rev*10 + dig
            x = math.trunc(x/10)
        return rev
