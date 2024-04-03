class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = dict()
        t_to_s = dict()
        for i in range(len(s)):
            cs, ts = s[i], t[i]
            if not cs in s_to_t:
                if ts in t_to_s:
                    return False
                s_to_t[cs] = ts
                t_to_s[ts] = cs
            else:
                if s_to_t[cs] != ts:
                    return False
        return True
