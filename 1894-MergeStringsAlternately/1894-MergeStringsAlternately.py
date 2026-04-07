# Last updated: 07/04/2026, 11:35:39
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k = []
        i , j = 0, 0 
        condition = (i <len(word1)-1 and j < len(word2)-1)



        while (i <len(word1) and j < len(word2)):
            k.append(word1[i])
            k.append(word2[j])
            i +=1
            j += 1 

        if i < len(word1):
            k.extend(word1[i:])
        elif j < len(word2):
            k.extend(word2[j:])

        return "".join(k)
