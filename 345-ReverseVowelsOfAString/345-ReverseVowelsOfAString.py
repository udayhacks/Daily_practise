# Last updated: 07/04/2026, 11:39:21
class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        s = list(s)

        vowels = "aeiouAEIOU"
        left_is_vowel, right_is_vowel = False, False # False meand need to check

        while left < right:
            if not left_is_vowel and s[left] not in vowels:
                left += 1
                continue
            else:
                left_is_vowel = True
            
            if not right_is_vowel and s[right] not in vowels:
                right -= 1
                continue
            else:
                right_is_vowel = True

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            left_is_vowel, right_is_vowel = False, False

        return "".join(s)
           
           
        