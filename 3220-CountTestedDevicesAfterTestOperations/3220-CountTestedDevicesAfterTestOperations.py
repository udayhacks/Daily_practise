# Last updated: 07/04/2026, 11:34:22
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int: 
        cnt = 0 
        for i in range(len(batteryPercentages)) :
            if batteryPercentages[i] > 0 :
                cnt+=1
                for j in range(i+1,len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
                    
        return cnt
        
        

        