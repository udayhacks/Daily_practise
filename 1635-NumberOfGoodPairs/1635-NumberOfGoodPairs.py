# Last updated: 07/04/2026, 11:36:07

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_counts = {}

    # Count the occurrences of each number
        for num in nums:
            if num in num_counts:
                count += num_counts[num]
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        return count