// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        A = tomatoSlices-2*cheeseSlices
        B = 4*cheeseSlices-tomatoSlices
        if A >=0 and A%2 == 0 and B >=0 and B%2 == 0:
            return [int(A/2), int(B/2)]
        return []