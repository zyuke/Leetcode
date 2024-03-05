// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                result = operations[token](num1, num2)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()