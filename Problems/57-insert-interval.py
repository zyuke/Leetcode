class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        brackets = []
        for interval in intervals:
            brackets.append((interval[0], 0))
            brackets.append((interval[1], 1))
        brackets.append((newInterval[0], 0))
        brackets.append((newInterval[1], 1))
        brackets.sort()

        stack = []
        res = []
        for b in brackets:
            if b[1] == 0:
                stack.append(b[0])
            if b[1] == 1:
                left = stack.pop()
                if not stack:
                    res.append([left, b[0]])

        return res
