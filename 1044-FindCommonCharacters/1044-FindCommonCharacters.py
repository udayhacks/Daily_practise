# Last updated: 07/04/2026, 11:37:12
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dd = defaultdict(int)
        l = []
        for word in words:
            d = defaultdict(int)
            for ch in word:
                d[ch] += 1
                dd[ch] += 1
            l.append(d)

        res = []
        for ch, freq in dd.items():
            mn = float("inf")
            for d in l:
                mn = min(mn, d[ch])

            if mn != 0:
                for _ in range(mn):
                    res.append(ch)

        return res