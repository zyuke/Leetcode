// https://leetcode.com/problems/top-k-frequent-elements

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for n in nums:
            try:
                freq[n] += 1
            except:
                freq[n] = 1
        
        s_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = [s_freq[i][0] for i in range(k)]
        
        return res