# Last updated: 07/04/2026, 11:36:40
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        winners, losers = {}, {}

        for match in matches:
            winner = match[0]
            loser = match[1]
            players.add(winner)
            players.add(loser)


            if loser in losers:
                losers[loser] += 1
            else:
                losers[loser] = 1

        zero_losses = []
        one_losses = []

        for player in sorted(players):
            if player not in losers:
                zero_losses.append(player)
            
            if player in losers and losers[player] == 1:
                one_losses.append(player)

        return [zero_losses, one_losses]