class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = len(temperatures)*[0]
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                top_i, _ = stack.pop()
                res[top_i] = i - top_i
            stack.append((i, t))

        return res
