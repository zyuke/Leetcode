# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeVals = []
        cur = head
        while cur:
            nodeVals.append(cur.val)
            cur = cur.next
        curMax = 0
        prevNode = None
        for v in reversed(nodeVals):
            if v >= curMax:
                curMax = v
                newNode = ListNode(v, prevNode)
                prevNode = newNode
        return prevNode
        
