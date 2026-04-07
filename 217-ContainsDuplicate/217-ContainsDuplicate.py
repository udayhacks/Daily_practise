# Last updated: 07/04/2026, 11:40:12

class Solution(object):
    def containsDuplicate(self, nums):
        s = set(nums)
        if len(s) != len(nums):
            return True
        
        return False
        