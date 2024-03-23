class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import defaultdict
        mp = defaultdict(lambda: 0)
        for t in tasks:
            mp[t] += 1
        max_freq = max(mp.values())
        ct_max_freq = 0
        for t in mp:
            if mp[t] == max_freq:
                ct_max_freq += 1
        time = (max_freq-1)*(n+1) + ct_max_freq
        return max(time, len(tasks))
