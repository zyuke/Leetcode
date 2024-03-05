// https://leetcode.com/problems/next-greater-node-in-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        N, vals = 0, []
        ct = head
        while ct:
            N += 1
            vals.append(ct.val)
            ct = ct.next
        
        stack, res = [], [0] * N
        for i in range(N):
            while stack and vals[stack[-1]] < vals[i]:
                res[stack.pop()] = vals[i]
            stack.append(i)
            
        return res
        