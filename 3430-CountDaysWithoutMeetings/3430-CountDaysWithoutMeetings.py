# Last updated: 07/04/2026, 11:34:07
class Solution:
    def countDays(self, days: int, meetings):
        
        
        
        
        meetings.sort()
        temp= [meetings[0]]
        
        for i in range(1,len(meetings)) :
            if temp[-1][1] >= meetings[i][0] :
                temp[-1][1] = max(meetings[i][1],temp[-1][1])
                
            else:
                temp.append(meetings[i])
        ans = 0 
        for i in temp :
            ans +=(( i[1]-i[0])+1) 
            
            
        return days-ans

