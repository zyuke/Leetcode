class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        num_group = []
        for i in range(len(nums)):
            for n in nums[i]:
                num_group.append([n, i])
        num_group.sort()

        from collections import defaultdict
        left, right = 0, 0
        group_ct = defaultdict(lambda: 0) 
        group_ct[num_group[0][1]] = 1
        
        min_size = float('inf')
        res = [num_group[0][0], num_group[0][0]]
        
        while True:
            if left == len(num_group)-1:
                break
            if len(group_ct) < len(nums):
                if right+1 < len(num_group):
                    right += 1
                    group_ct[num_group[right][1]] += 1
                    continue
                else:
                    break
            if len(group_ct) == len(nums):
                if num_group[right][0]-num_group[left][0] < min_size:
                    min_size = num_group[right][0]-num_group[left][0] 
                    res = [num_group[left][0], num_group[right][0]]
                if left == right:
                    break
                group_ct[num_group[left][1]] -= 1
                if group_ct[num_group[left][1]] == 0:
                    del group_ct[num_group[left][1]]
                left += 1 

        return res
