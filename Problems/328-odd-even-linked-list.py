// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        odd_head, odd_ptr = head, head
        even_head, even_ptr = head.next, head.next
        
        while True:
            if odd_ptr:
                if odd_ptr.next and odd_ptr.next.next:
                    odd_ptr.next = odd_ptr.next.next
                    odd_ptr = odd_ptr.next
            if even_ptr:
                if even_ptr.next:
                    even_ptr.next = even_ptr.next.next
                    even_ptr = even_ptr.next
                else:
                    break
            if not even_ptr:
                break
                
        odd_ptr.next = even_head
        return odd_head