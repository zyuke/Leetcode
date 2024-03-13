# https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 == 1:
            return False
        
        n = len(nums)
        T = int(S / 2)
        table = []
        for i in range(n + 1):
            table.append([0] * (T + 1))
            
        table[0][0] = 1
        for i in range(1, n+1):
            table[i][0] = 1
        for j in range(1, T+1):
            table[0][j] = 0
            
        for i in range(1, n+1):
            for j in range(1, T+1):
                table[i][j] = table[i-1][j]
                if nums[i-1] <= j:
                    table[i][j] = table[i][j] or table[i-1][j-nums[i-1]]
                    
        return table[-1][-1]
            
        