# Last updated: 07/04/2026, 11:35:51

class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:

        x = Counter(word1)

        y = Counter(word2)

        a = Counter(x.values())

        b = Counter(y.values())

        c = a - b

        return x.keys() == y.keys() and len(c) == 0