# Last updated: 07/04/2026, 11:38:52



class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        hash = {}
        for i in range(len(nums2)):
            k = -1
            for j in range(i+1,len(nums2)):
                if nums2[i]<nums2[j] :
                    k= nums2[j]
                    break
                    
            hash[nums2[i]] = k 

        ans = []
        for i in nums1:
            ans.append(hash[i])
        
        return ans
        