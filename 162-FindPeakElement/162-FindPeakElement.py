# Last updated: 07/04/2026, 11:40:42
"""class Solution:
    def findPeakElement(self, nums: List[int]) -> int:



        l = 1
        n = len(nums)-1
        h = n-2

        if n <= 3 :
            return nums.index(max(nums))

     

        while l <=h :
            m = (l+h)//2

            if (nums[m-1]<= nums[m]) and (nums[m+1] <=nums[m]) :
                return m
            if m> 0 and nums[m-1] > nums[m] :
                h = m-1
            else :
                l = m+1
        return -1 



"""

































class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        l = 1
        h = n - 2
        while l <= h:
            m = (l + h) // 2
            if nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m

            if nums[m] > nums[m - 1]:
                l = m + 1

            else:
                h = m - 1

        return -1



        