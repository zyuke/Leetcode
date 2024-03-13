# https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
        
        def update_output(cur_pos):
            segment = s[cur_pos+1:]
            if is_valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()
        
        def backtrack(prev_pos = -1, dots = 3):
            for cur_pos in range(prev_pos+1, min(n-1, prev_pos+4)):
                segment = s[prev_pos+1:cur_pos+1]
                if is_valid(segment):
                    segments.append(segment)
                    if dots == 1:
                        update_output(cur_pos)
                    else:
                        backtrack(cur_pos, dots-1)
                    segments.pop()
        
        n = len(s)
        output, segments = [], []
        backtrack()
        return output