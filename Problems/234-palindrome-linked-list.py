# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        L = []
        iterator = head
        while iterator != None:
            L.append(iterator.val)
            iterator = iterator.next
        
        n = len(L)
        for i in range(n/2):
            if L[i] != L[n-i-1]:
                return False
        
        return True