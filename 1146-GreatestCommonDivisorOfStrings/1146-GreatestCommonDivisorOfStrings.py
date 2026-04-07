# Last updated: 07/04/2026, 11:36:58
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1+str2 != str2+str1: return "" 
        # divisor = math.gcd(len(str1), len(str2))
        # return str1[:divisor]

    #Solution 2
        if str1+str2 != str2+str1: return "" 
        divisor = self.gcd(len(str1), len(str2))
        return str1[:divisor]

    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a

        
        