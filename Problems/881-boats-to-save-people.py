class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        res = 0
        while left < right:
            if people[right] + people[left] <= limit:
                res += 1
                left += 1
                right -= 1
            else:
                res += 1
                right -= 1
        if left == right:
            res += 1
        return res

