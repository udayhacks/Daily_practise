# Last updated: 07/04/2026, 11:38:26
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    c+=1
            if i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]!=1:
                    flowerbed[i]=1
                    c+=1
            if flowerbed[i]==1:
                continue
            else:
                if flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    c+=1
        if c>=n:
            return True
        else:
            return False
            