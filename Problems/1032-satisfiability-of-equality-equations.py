// https://leetcode.com/problems/satisfiability-of-equality-equations

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        group = [[] for i in range(26)]
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                group[x].append(y)
                group[y].append(x)
                
        color = [None] * 26
        count = 0
        for cur in range(26):
            if color[cur] == None:
                count += 1
                stack = [cur]
                while stack:
                    node = stack.pop()
                    for nxt in group[node]:
                        if color[nxt] == None:
                            color[nxt] = count
                            stack.append(nxt)
        print(group)                    
        print(color)
                            
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if x == y:
                    return False
                if color[x] is not None and color[x] == color[y]:
                    return False
        
        return True