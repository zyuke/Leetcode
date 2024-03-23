# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = deque([])
        s = ''
        for c in data:
            if c == ',':
                queue.append(s)
                s = ''
            else:
                s += c
        if s:
            queue.append(s)
        return self.helper(queue)

    def helper(self, queue):
        if not queue:
            return None
        s = queue.popleft()
        if s == '#':
            return None
        node = TreeNode(int(s))
        node.left = self.helper(queue)
        node.right = self.helper(queue)
        return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
