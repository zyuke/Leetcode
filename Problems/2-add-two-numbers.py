// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(None)
        cur = ret
        carry = 0
        
        while l1 or l2:
            if not l1 and l2:
                digit_sum = l2.val + carry
                l2 = l2.next
            if not l2 and l1:
                digit_sum = l1.val + carry
                l1 = l1.next
            if l1 and l2:
                digit_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            if digit_sum > 9:
                carry = 1
                node_val = digit_sum % 10
            else:
                carry = 0
                node_val = digit_sum
            
            node = ListNode(node_val)
            cur.next = node
            cur = cur.next
        
        if carry == 1:
            node = ListNode(1)
            cur.next = node
            cur = cur.next
        
        return ret.next
                