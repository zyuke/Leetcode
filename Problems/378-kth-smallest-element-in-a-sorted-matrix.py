# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        vec = []
        for i in matrix:
            vec += i
        vec_sort = sorted(vec)
        return vec_sort[k-1]