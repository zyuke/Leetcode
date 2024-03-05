// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = sum(nums[:k])
        cur_set = defaultdict(lambda: 0)
        for i in range(k):
            cur_set[nums[i]] += 1
        max_sum = 0
        if len(cur_set) == k:
            max_sum = cur_sum
        for idx in range(k, len(nums)):
            # print(cur_set)
            cur_sum += nums[idx]
            cur_sum -= nums[idx-k]
            cur_set[nums[idx-k]] -= 1
            if cur_set[nums[idx-k]] == 0:
                del cur_set[nums[idx-k]]
            cur_set[nums[idx]] += 1
            if len(cur_set) == k:
                max_sum = max(max_sum, cur_sum)
        
        return max_sum