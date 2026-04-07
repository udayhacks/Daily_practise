# Last updated: 07/04/2026, 11:36:14
# Constant Dictionary of characters: vowels are 1, others are 0 (default)
VOWELS = defaultdict(int)
VOWELS['a'] = VOWELS['e'] = VOWELS['i'] = VOWELS['o'] = VOWELS['u'] = 1

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        Replace characters in s with an int value: 1 for vowels, 0 otherwise.
        We'll return the maximum sum of any k-length window on s. 
        '''
        s = [VOWELS[c] for c in s]
        max_count = count = sum(s[:k])      # Both counts hold the initial sum
        for i in range(len(s) - k):         # Advance the window
            count += s[i + k] - s[i]        # Adjust the count
            if count > max_count:           # Keep the higher count
                max_count = count
        return max_count

            