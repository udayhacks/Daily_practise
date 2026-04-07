# Last updated: 07/04/2026, 11:36:00
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        big_piles = sorted_piles[int(len(piles)/3):]
        maxxed = sum(big_piles[::2])
        return maxxed