from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x: int, y: int) -> int:
            len_x = len(str(x))
            len_y = len(str(y))
            xy = x*10**len_y + y
            yx = y*10**len_x + x
            if xy > yx:
                return 1
            if xy < yx:
                return -1
            return 0
        if nums[0] == 0 and len(set(nums)) == 1:
            return '0'
        nums.sort(key=cmp_to_key(cmp), reverse=True)
        res = ''
        for n in nums:
            res += str(n)
        return res
