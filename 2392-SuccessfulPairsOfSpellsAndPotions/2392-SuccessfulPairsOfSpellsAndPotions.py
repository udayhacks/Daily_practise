# Last updated: 07/04/2026, 11:35:06
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []

        for spell in spells:
            min_potion = math.ceil(success/spell)
            l, r, success_potions = 0, len(potions)-1, 0

            while l <= r:
                mid = (l+r) // 2
                if potions[mid] >= min_potion:
                    success_potions += (r-mid+1)
                    r = mid - 1
                else:
                    l = mid + 1

            pairs.append(success_potions)

        return pairs