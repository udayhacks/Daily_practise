# Last updated: 07/04/2026, 11:34:32
class Solution:

    def isAcronym(self, words: List[str], s: str) -> bool:

        acronym=''.join(i[0] for i in words)

        return acronym==s
