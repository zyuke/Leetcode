// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        ite = head
        while ite:
            ite = ite.next
            length += 1
        
        if n == length:
            return head.next
        else:
            res = head
            cur = head
            p = length - n
            while p != 0:
                prev = cur
                cur = cur.next
                p -= 1
            
            prev.next = cur.next
            return res