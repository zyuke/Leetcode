# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return False
            else:
                res = helper(node.next)
                node.val *= 2
                if res:
                    node.val += 1
                if node.val >= 10:
                    node.val -= 10
                    return True
                return False
        
        res = helper(head)
        if res:
            head = ListNode(1, head)
        return head
        
