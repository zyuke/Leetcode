# https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = sorted(nums1)
        l2 = sorted(nums2)
        n1 = len(l1)
        n2 = len(l2)
        result = []
        
        iter1 = 0; iter2 = 0
        while iter1 != n1 and iter2 != n2:
            if l1[iter1] == l2[iter2]:
                result.append(l1[iter1])
                iter1 += 1; iter2 += 1
            elif l1[iter1] > l2[iter2]:
                iter2 += 1
            elif l1[iter1] < l2[iter2]:
                iter1 += 1
        
        return result