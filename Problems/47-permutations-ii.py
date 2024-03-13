# https://leetcode.com/problems/permutations-ii

class Solution:
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        D = {}
        res = []
        def helper(cur_list, D):
            if len(D) == 0:
                res.append(cur_list)
            else:
                for k in D:
                    new_cur_list = cur_list.copy()
                    new_cur_list.append(k)
                    new_D = D.copy()
                    new_D[k] -= 1
                    if new_D[k] == 0:
                        del new_D[k]
                    helper(new_cur_list, new_D)
        for i in nums:
            try:
                D[i] += 1
            except:
                D[i] = 1
        helper([], D)
        return res
    
        