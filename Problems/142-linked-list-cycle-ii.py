// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        meet = None
        slow, fast = head, head
        
        while fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                break
            if fast == slow:
                meet = slow
                break
                
        if meet:
            a1, a2 = head, meet
            while True:
                if a1 == a2:
                    res = a1
                    break
                a1 = a1.next
                a2 = a2.next
                    
        return res