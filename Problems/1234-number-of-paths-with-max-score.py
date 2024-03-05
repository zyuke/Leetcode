// https://leetcode.com/problems/number-of-paths-with-max-score

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        BOARD = [b[::-1] for b in board[::-1]]
        board = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                try:
                    board[i][j] = int(BOARD[i][j])
                except:
                    board[i][j] = 0
                    
        DP_score = [[0] * n for _ in range(n)]
        
        # initialize first row of DP_score
        obstacle = False
        for i in range(1, n):
            if obstacle:
                DP_score[0][i] = 0
            else:
                if board[0][i] == 0:
                    obstacle = True
                    DP_score[0][i] = 0
                    continue
                DP_score[0][i] = board[0][i] + DP_score[0][i-1]
        # initialize first column of DP_score
        obstacle = False
        for i in range(1, n):
            if obstacle:
                DP_score[i][0] = 0
            else:
                if board[i][0] == 0:
                    obstacle = True
                    DP_score[i][0] = 0
                    continue
                DP_score[i][0] = board[i][0] + DP_score[i-1][0]
        
        # fill the DP_score table
        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] == 0 and not (i == n-1 and j == n-1):
                    DP_score[i][j] = 0      
                else:
                    if i ==1 and j == 1:
                        score_right = 0 if DP_score[i][j-1] == 0 else DP_score[i][j-1] + board[i][j]
                        score_down = 0 if DP_score[i-1][j] == 0 else DP_score[i-1][j] + board[i][j]
                        score_diag = board[i][j]
                        DP_score[i][j] = max(score_right, score_down, score_diag)
                    else:
                        score_right = 0 if DP_score[i][j-1] == 0 else DP_score[i][j-1] + board[i][j]
                        score_down = 0 if DP_score[i-1][j] == 0 else DP_score[i-1][j] + board[i][j]
                        score_diag = 0 if DP_score[i-1][j-1] == 0 else DP_score[i-1][j-1] + board[i][j]
                        DP_score[i][j] = max(score_right, score_down, score_diag)
        
        
        if DP_score[n-1][n-1] == 0 and n > 2:
            return (0, 0)
        
        # find number of paths to the maximum score
        DP_path = [[0] * n for _ in range(n)]
        DP_path[0][0] = 1
        # initialize first row of DP_path
        obstacle = False
        for i in range(1, n):
            if obstacle:
                DP_path[0][i] = 0
            else:
                if board[0][i] == 0:
                    obstacle = True
                    DP_path[0][i] = 0
                    continue
                DP_path[0][i] = 1
        # initialize first column of DP_path
        obstacle = False
        for i in range(1, n):
            if obstacle:
                DP_path[i][0] = 0
            else:
                if board[i][0] == 0:
                    obstacle = True
                    DP_path[i][0] = 0
                    continue
                DP_path[i][0] = 1
        
        # fill the DP_path table
        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] == 0 and not (i == n-1 and j == n-1):
                    DP_path[i][j] = 0
                else:
                    right, down, diag = 0, 0, 0
                    if DP_path[i][j-1] != 0 and DP_score[i][j] == board[i][j] + DP_score[i][j-1]:
                        right = DP_path[i][j-1]
                    if DP_path[i-1][j] != 0 and DP_score[i][j] == board[i][j] + DP_score[i-1][j]:
                        down = DP_path[i-1][j]
                    if DP_path[i-1][j-1] != 0 and DP_score[i][j] == board[i][j] + DP_score[i-1][j-1]:
                        diag = DP_path[i-1][j-1]
                    DP_path[i][j] = (right + down + diag)

        print(DP_path)
        
        return (DP_score[n-1][n-1], DP_path[n-1][n-1] % 1000000007)
            