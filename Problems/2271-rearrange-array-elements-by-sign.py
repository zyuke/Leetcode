# https://leetcode.com/problems/rearrange-array-elements-by-sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [n for n in nums if n > 0]
        neg = [n for n in nums if n < 0]
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res