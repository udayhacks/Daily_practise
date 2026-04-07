# Last updated: 07/04/2026, 11:39:15
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        visit = set()
        res= []
        i = j = 0
        heap.append(((nums1[i]+nums2[j],i,j)))
        visit.add((i,j)) 
        
        while k and heap :
            a,i,j = heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])

            if i+1 <len(nums1) and (i+1,j) not in visit :
                heapq.heappush(heap,((nums1[i+1]+nums2[j]),i+1,j))
                visit.add((i+1,j)) 
            if j+1 < len(nums2) and (i,j+1) not in visit :
               
                heapq.heappush(heap,((nums1[i]+nums2[j+1]),i,j+1))
                visit.add((i,j+1)) 
            k-=1


        return res





        