# https://leetcode.com/problems/robot-return-to-origin

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = 0; w =0
        for i in range(len(moves)):
            if moves[i]=='U':
                h +=1
            elif moves[i]=='D':
                h -=1
            elif moves[i]=='L':
                w -=1
            elif moves[i]=='R':
                w +=1
        if h == 0 and w == 0:
            return True
        else:
            return False
                