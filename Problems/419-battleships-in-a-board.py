// https://leetcode.com/problems/battleships-in-a-board

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        M = len(board)
        N = len(board[0])
        
        res = 0
        
        for i in range(M):
            for j in range(N):
                if board[i][j] == ".":
                    pass
                elif board[i][j] == "X":
                    if (i == 0 and j == 0) or (i == 0 and board[i][j-1] == '.') or (j == 0 and board[i-1][j] == ".") or (board[i][j-1] == '.' and board[i-1][j] == "."):
                        res += 1
                        
        return res