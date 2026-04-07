# Last updated: 07/04/2026, 11:43:16
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash = {

            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        ans = []
        def backtrack(i,curr):
            if  len(curr)== len(digits) :
                ans.append(curr)
                return 
            for c in hash[digits[i]] :
                backtrack(i+1,curr+c)


            return ans



        if digits :
            backtrack(0,'')

        return ans


          
