# Last updated: 07/04/2026, 11:35:13
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = [s.count('1') for s in bank if s.count('1') != 0]
        return sum([counts[i]*counts[i+1] for i in range(len(counts)-1)])