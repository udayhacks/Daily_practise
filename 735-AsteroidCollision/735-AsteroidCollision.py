# Last updated: 07/04/2026, 11:38:08
class Solution:
    def asteroidCollision(self, asteroids):
        res = []

        for a in asteroids:
            while res and a < 0 < res[-1]:
                if -a > res[-1]:  # Current asteroid wins
                    res.pop()
                    continue
                elif -a == res[-1]:  # Both explode
                    res.pop()
                break
            else:  # No collision
                res.append(a)

        return res