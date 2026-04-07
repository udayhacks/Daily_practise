# Last updated: 07/04/2026, 11:34:37
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        stack = []
        bots = []

        for i in range(n):
            bots.append((i, positions[i], healths[i], directions[i]))

        bots.sort(key= lambda x: x[1])

        for bot in bots:
            i, p, h, d = bot
            if d == 'R':
                stack.append(bot)
                continue
            while stack and stack[-1][3] == 'R' and h > 0:
                if stack[-1][2] == h:
                    stack.pop()
                    h = 0
                elif stack[-1][2] < h:
                    stack.pop()
                    h -= 1
                else:
                    stack[-1] = (stack[-1][0], stack[-1][1], stack[-1][2] - 1, stack[-1][3])
                    h = 0
            if h > 0:
                stack.append((i, p, h, d))
        stack.sort(key= lambda x: x[0])
        return [bot[2] for bot in stack]