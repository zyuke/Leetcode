class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        cur_sum, cur_best, cur_num = 0, 0, 0
        for score in satisfaction:
            new_best = score + cur_sum + cur_best
            if new_best >= cur_best:
                cur_best = new_best
                cur_sum += score
                cur_num += 1

        return cur_best
