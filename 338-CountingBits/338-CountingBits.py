# Last updated: 07/04/2026, 11:39:24
class Solution:
    def countBits(self, n: int) -> List[int]:
        cache = [0]
        for i in range(1, n+1):
            cache.append(cache[i>>1] +i %2)

        return cache

