class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ct = 0
        for x in arr:
            if x % 2 == 1:
                ct +=1
            else:
                ct = 0
            if ct == 3:
                return True
        return False
