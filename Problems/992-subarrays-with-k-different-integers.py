from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def ct_atmost_k(nums, k):
            ct = defaultdict(int)
            left, right, res = 0, 0, 0
            while right < len(nums):
                ct[nums[right]] += 1
                while len(ct) > k:
                    ct[nums[left]] -= 1
                    if ct[nums[left]] == 0:
                        del ct[nums[left]]
                    left += 1
                res +=  right - left + 1
                right += 1
            return res
        
        return ct_atmost_k(nums, k) - ct_atmost_k(nums, k-1)
                        
