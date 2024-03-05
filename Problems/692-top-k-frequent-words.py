// https://leetcode.com/problems/top-k-frequent-words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        word_count = Counter(words)
        heap = [(-freq, word) for word, freq in word_count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]