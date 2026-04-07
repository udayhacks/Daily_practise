# Last updated: 07/04/2026, 11:40:34
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        start,end=0,10
        d={}
        while end<len(s)+1:
            slide=s[start:end]
            if slide not in d:
                d[slide]=1
            else:
                d[slide]+=1
            start+=1
            end+=1
        l=[]
        for i in d:
            if d[i]>=2:
                l.append(i)
        return l