// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints)-k
        if window_size == 0:
            return sum(cardPoints)
    
        cur_sum = sum(cardPoints[:window_size])
        min_window_sum = cur_sum
        
        for l in range(1, len(cardPoints)-window_size+1):
            new_sum = cur_sum - cardPoints[l-1] + cardPoints[l+window_size-1]
            cur_sum = new_sum
            min_window_sum = min(min_window_sum,cur_sum)
        
        return sum(cardPoints) - min_window_sum
        
        