// https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head.next
        cur_sum = 0
        new_nodes = []
        
        while cur_node:
            if cur_node.val == 0:
                new_nodes.append(ListNode(cur_sum))
                cur_sum = 0
            else:
                cur_sum += cur_node.val
            cur_node = cur_node.next
        
        for i in range(len(new_nodes)-1):
            new_nodes[i].next = new_nodes[i+1]
        
        return new_nodes[0]
        