class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        def search(idx, curStr, val, last):
            if idx == n and val == target:
                res.append(curStr)
            for nextIdx in range(idx+1, n+1):
                curNum = int(num[idx:nextIdx])
                if nextIdx == idx + 1 or (nextIdx > idx + 1 and num[idx] != '0'):
                    if last == None:
                        search(nextIdx, num[idx:nextIdx], curNum, curNum)
                    else:
                        search(nextIdx, curStr+'+'+num[idx:nextIdx], val+curNum, curNum)
                        search(nextIdx, curStr+'-'+num[idx:nextIdx], val-curNum, -curNum)
                        search(nextIdx, curStr+'*'+num[idx:nextIdx], val-last+last*curNum, last*curNum)

        search(0, '', 0, None)
        return res
