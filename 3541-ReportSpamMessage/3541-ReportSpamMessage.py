# Last updated: 07/04/2026, 11:33:58
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = set(bannedWords)
        count = 0

        for msg in message:
            if msg in banned:
                count += 1
                if count == 2:
                    return True
        return False
                
            

            
        