class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_num = sorted(nums1+nums2)
        N = len(new_num)
        if N%2==0:
            l = N//2-1
            r = N//2
            return (new_num[l]+new_num[r])/2
        else:
            return new_num[N//2]
