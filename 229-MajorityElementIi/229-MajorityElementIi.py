# Last updated: 07/04/2026, 11:40:04
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1 = -float("inf")
        e2 = -float("inf")

        c1 = c2 = 0

        if len(nums) <3 :
            return list(set(nums))
            
    

        
        for i in nums:
            
            if c1 == 0 and i != e2  :
                e1 = i 
                c1 = 1

            elif c2 == 0 and i != e1 :
                e2 = i 
                c2 = 1

            elif i == e1 : c1+=1
            elif i == e2 : c2+=1
            else:
                c1-=1
                c2-=1


        

        m = int(len(nums)/3)+1

        c1 = c2 = 0 

        for i in nums :
            if e1 == i :
                c1 +=1 
            elif e2 ==i :
                c2 +=1
        ans = []
        if c1 >= m :
            ans.append(e1)
        if c2 >= m :
            ans.append(e2) 


        return ans

        
        