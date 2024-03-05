// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        nums = [0] + nums + [0]
        N = len(nums)
        left_sum = [0] * N
        right_sum = [0] * N
        l, r = 0, 0
        for i in range(N):
            l += nums[i]
            r += nums[N-1-i]
            left_sum[i] = l
            right_sum[N-1-i] = r
        
        from bisect import bisect_left
        res = float('inf')
        found = False
        for l_idx in range(N):
            r_idx = bisect_left(right_sum, -1*(x-left_sum[l_idx]), l_idx+1, N, key=lambda x: -1*x)
            if r_idx != N and right_sum[r_idx] + left_sum[l_idx] == x:
                found = True
                step = N-(r_idx-l_idx)+1
                if step < res:
                    res = step

        return res-2 if found else -1
