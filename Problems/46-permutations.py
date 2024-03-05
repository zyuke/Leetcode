// https://leetcode.com/problems/permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from copy import deepcopy
        res = []
        
        def dfs(toapp, cur, res):
            if cur == []:
                res.append(toapp)
                return
            else:
                for x in cur:
                    nxtapp = deepcopy(toapp)
                    nxtapp.append(x)
                    nxt = deepcopy(cur)
                    nxt.remove(x)
                    dfs(nxtapp, nxt, res)
                    
        dfs([], nums, res)
        return res