# Last updated: 07/04/2026, 11:37:46
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            first_card = min_heap[0]
            for i in range(first_card, first_card + groupSize):
                if card_count[i] == 0:
                    return False
                card_count[i] -= 1
                if card_count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True