# Last updated: 07/04/2026, 11:39:42
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i, j in enumerate(sorted(citations, reverse=True)):
            if i >= j:
                return i
        return i + 1
     