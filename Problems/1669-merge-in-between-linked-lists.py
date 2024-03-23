# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l2_head = list2
        l2_tail = list2
        while l2_tail.next:
            l2_tail = l2_tail.next

        left, right = list1, list1
        cur = list1
        cur_n = 1
        while cur:
            if cur_n == a:
                left = cur
            if cur_n == b:
                right = cur.next.next
                break
            cur = cur.next
            cur_n += 1
        
        left.next = l2_head
        l2_tail.next = right
        return list1
