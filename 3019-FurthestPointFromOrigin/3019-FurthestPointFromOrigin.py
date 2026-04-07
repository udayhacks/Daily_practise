# Last updated: 07/04/2026, 11:34:31
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
                  

        d = {'L':0,'R':0,'_':0}
        ans = v = 0 

        for i in moves :
            if i in d :
                d[i] +=1
          

        if  d['_'] == len(moves) :
            return len(moves)

        else:
            if d['L'] >= d['R'] :
                d["_"] *=-1
            if "_" in d :
                print("l")

            return abs(d['R'] -d['L'] +d['_'])