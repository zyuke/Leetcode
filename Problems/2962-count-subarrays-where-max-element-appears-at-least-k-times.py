class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        max_n = max(nums) 
        i, j, ct, res = 0, 0, 0, 0

        while j < N:
            if nums[j] == max_n:
                ct += 1
            while ct >= k:
                res += N - j
                if nums[i] == max_n:
                    ct -= 1
                i += 1
            j += 1

        return res
        
