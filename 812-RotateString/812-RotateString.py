# Last updated: 07/04/2026, 11:37:58
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in (goal+goal)
        
        