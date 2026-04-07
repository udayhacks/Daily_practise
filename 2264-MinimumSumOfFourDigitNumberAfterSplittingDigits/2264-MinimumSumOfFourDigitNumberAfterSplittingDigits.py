# Last updated: 07/04/2026, 11:35:11
class Solution:
  def minimumSum(self, num: int) -> int:
    num = sorted(str(num))
    m = num[0] + num[2]
    n = num[1] + num[3]
    return int(m) + int(n)