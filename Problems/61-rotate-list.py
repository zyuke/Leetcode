// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
            
        node_idx = 0
        start = head
        idx2node = {}
        while start != None:
            idx2node[node_idx] = start
            node_idx += 1
            start = start.next
        k_mod = k % node_idx

        if k_mod == 0:
            return head
        new_last = idx2node[node_idx-k_mod-1]
        res = new_last.next
        new_last.next = None
        idx2node[node_idx-1].next = head
        return res