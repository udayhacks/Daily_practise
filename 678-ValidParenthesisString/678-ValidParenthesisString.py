# Last updated: 07/04/2026, 11:38:17
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_cnt, close_cnt = 0, 0
        R = len(s) - 1
        for i, c in enumerate(s):
            if c == '(' or c == '*':
                open_cnt += 1
            else:
                open_cnt -= 1
            
            if s[R - i] == ')' or s[R - i] == '*':
                close_cnt += 1
            else:
                close_cnt -= 1
            
            if open_cnt < 0 or close_cnt < 0:
                return False
        return True
            