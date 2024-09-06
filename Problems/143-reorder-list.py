# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_map = {}
        ct = 0
        cur_node = head
        while cur_node:
            node_map[ct] = cur_node
            ct += 1

        new_head = ListNode()
        cur_node = new_head
        for i in range(ct):
            if i % 2 == 0:
                cur_node.next = node_map[int(i/2)] 
            else:
                cur_node.next = node_map[ct-int((i-1)/2)]
            cur_node = cur_node.next
