import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-1*n for n in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            val = -1*heapq.heappop(nums)
            res += val
            val = ceil(val/3)
            heapq.heappush(nums, -1*val)

        return res
