// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        aliceScore = 0
        bobScore = 0
        aScore, bScore = 0, 0
        for c in colors:
            if c == 'A':
                if aScore != 0:
                    aScore += 1
                else:
                    aScore = 1
                    bobScore += max(0, bScore - 2)
                    bScore = 0
            if c == 'B':
                if bScore != 0:
                    bScore += 1
                else:
                    bScore = 1
                    aliceScore += max(0, aScore - 2)
                    aScore = 0
        bobScore += max(0, bScore - 2)
        aliceScore += max(0, aScore - 2)

        return aliceScore > bobScore