# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        head = ListNode(None)
        Q = PriorityQueue()
        
        for node in lists:
            if node:
                Q.put((node.val, id(node), node))
        
        cur = head
        while Q.qsize() > 0:
            cur.next = Q.get()[2]
            cur = cur.next
            if cur.next:
                Q.put((cur.next.val, id(cur.next), cur.next))
            
        return head.next
            