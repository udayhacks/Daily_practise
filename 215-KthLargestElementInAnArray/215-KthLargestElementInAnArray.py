# Last updated: 07/04/2026, 11:40:13
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)) :
           nums[i] = -nums[i]

        heapq.heapify(nums)
        while k >1 :
            heapq.heappop(nums)
            k-=1
        return -heapq.heappop(nums)


        

        