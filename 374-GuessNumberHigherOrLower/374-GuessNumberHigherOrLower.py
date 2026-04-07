# Last updated: 07/04/2026, 11:39:14
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while(low <= high):
            pick = (low + high) // 2

            if guess(pick) == 0:
                return pick
            if guess(pick) == -1:
                high = pick - 1
            else:
                low = pick + 1