// https://leetcode.com/problems/parsing-a-boolean-expression

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def NOT(exp):
            if exp[0] == 't':
                return 'f'
            if exp[0] == 'f':
                return 't'
        def AND(exp):
            for e in exp:
                if e == 'f':
                    return 'f'
            return 't'
        def OR(exp):
            for e in exp:
                if e == 't':
                    return 't'
            return 'f'
        
        stack = []
        for e in expression:
            # print(stack)
            if e == ')':
                exp = []
                while True:
                    c = stack.pop()
                    if c == 't' or c == 'f':
                        exp.append(c)
                    elif c == '(':
                        func = stack.pop()
                        if func == '!':      
                            val = NOT(exp)
                            stack.append(val)
                            break
                        if func == '|':
                            val = OR(exp)
                            stack.append(val)
                            break
                        if func == '&':
                            val = AND(exp)
                            stack.append(val)
                            break
                    else:
                        continue
            else:
                stack.append(e)
                
        return True if stack[0] == 't' else False