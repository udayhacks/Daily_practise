# Last updated: 07/04/2026, 11:41:07
class Solution:
    
    def is_pal(self,s,i ,j) :
        while i <= j :
            if s[i]!= s[j] :
                return False

            i+=1
            j-=1
        return True


    def func(self,s,index,path,res) :
        if (index == len(s)):
            res.append(path[:])
            return 

        for i in range(index,len(s)):
            if self.is_pal(s,index,i) :
                path.append(s[index:i+1])
                self.func(s,i+1,path,res)
                path.pop()

            



    
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res=[]
        self.func(s,0,path,res)
        return res



        
        