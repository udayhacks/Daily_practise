# Last updated: 07/04/2026, 11:42:44
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:




        n = len(nums) 
        if n == 1   :
            if nums[-1] == target :
                return [0,0] 
            else :
                return [-1,-1]
         


        def f_search (self,nums, target ) :
            n = len(nums)
            l = 0 
            h = n-1 
            while l <= h :
                m = (l+h)//2 

                if nums[m] == target :
                    if m == 0 or  nums[m-1] != target  :
                        return m 
                    else :
                        h = m-1
                        continue

                if target > nums[m] :
                    l = m+1
                else :
                    h =  m-1
            return -1





        def b_search (self,nums, target ) :
            n = len(nums)
            l = 0 
            h = n-1 
            while l <= h :
                m = (l+h)//2 

                if nums[m] == target :
                    if   m == n-1 or nums[m+1] != target   :
                        return m 
                    else :
                        l = m+1
                        continue

                if target > nums[m] :
                    l = m+1
                else :
                    h =  m-1  

            return -1 





        return [f_search (self,nums, target ) ,b_search (self,nums, target ) ]

                






                            