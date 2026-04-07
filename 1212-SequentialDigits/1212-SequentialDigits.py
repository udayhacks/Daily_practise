# Last updated: 07/04/2026, 11:36:51
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lst = []

        for i in range(1,10):
            num = i
            next_num = i

            #Adding next digit to number
            while num <= high and next_num < 10:
                if num >= low:
                    lst.append(num)

                next_num += 1
                num = num * 10 + next_num
        return sorted(lst)