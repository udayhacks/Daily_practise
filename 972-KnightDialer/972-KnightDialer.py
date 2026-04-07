# Last updated: 07/04/2026, 11:37:30
class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        MOD = 10 ** 9 + 7
        for _ in range(n-1):
            temp = [0] * 10
            temp[0] = (dp[4] + dp[6]) % MOD
            temp[1] = (dp[6] + dp[8]) % MOD
            temp[2] = (dp[7] + dp[9]) % MOD
            temp[3] = (dp[4] + dp[8]) % MOD
            temp[4] = (dp[0] + dp[3] + dp[9]) % MOD
            temp[5] = 0
            temp[6] = (dp[0] + dp[1] + dp[7]) % MOD
            temp[7] = (dp[2] + dp[6]) % MOD
            temp[8] = (dp[1] + dp[3]) % MOD
            temp[9] = (dp[2] + dp[4]) % MOD
            dp = temp
        return sum(dp) % MOD