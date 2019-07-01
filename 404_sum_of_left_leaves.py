# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.inner(root, False)
        
    def inner(self, root, isleft):
        if not root:
            return 0
        elif not root.left and not root.right:
            if isleft:
                return root.val
            return 0
        else:
            return self.inner(root.left, True) + self.inner(root.right, False)