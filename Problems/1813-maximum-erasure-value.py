// https://leetcode.com/problems/maximum-erasure-value

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur_max = 0 
        cur_sum = 0
        total_sum = 0
        cur_idx = 0
        sum_upto_id = []
        last_seen_pos = {}
        
        for i in range(len(nums)):
            total_sum += nums[i]
            sum_upto_id.append(total_sum)
            if nums[i] not in last_seen_pos:
                cur_sum += nums[i]
                last_seen_pos[nums[i]] = i
            else:
                if last_seen_pos[nums[i]] >= cur_idx:
                    if cur_sum > cur_max:
                        cur_max = cur_sum
                    cur_idx = last_seen_pos[nums[i]] + 1
                    cur_sum = sum_upto_id[i] - sum_upto_id[last_seen_pos[nums[i]]]
                    last_seen_pos[nums[i]] = i
                else:
                    cur_sum += nums[i]
                    last_seen_pos[nums[i]] = i
            if cur_sum > cur_max:
                    cur_max = cur_sum
        
        return cur_max