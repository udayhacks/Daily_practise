# Last updated: 07/04/2026, 11:36:43
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = {}

        for i in arr :
            if i in hash:
                hash[i] +=1
            else:
                hash[i] = 1

        return len(hash.values()) == len(set(hash.values()))
        