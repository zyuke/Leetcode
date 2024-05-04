# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        buckets = []
        bucket = []
        curNode = head
        while curNode:
            bucket.append(curNode)
            if len(bucket) == k:
                buckets.append(bucket)
                bucket = []
            curNode = curNode.next
        if bucket:
            buckets.append(bucket)

        for b in buckets:
            if len(b) == k:
                for i in range(len(b)-1, 0, -1):
                    b[i].next = b[i-1]
                b[0].next = None
            if len(b) < k:
                b.reverse() 

        for i in range(len(buckets)-1):
            buckets[i][0].next = buckets[i+1][-1]

        return buckets[0][-1]

