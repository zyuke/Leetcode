// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        initial_state = grid[0]
        row_reverse = [int(not x) for x in initial_state]
        for row in grid:
            if row == initial_state or row == row_reverse:
                continue
            else:
                return False
        return True