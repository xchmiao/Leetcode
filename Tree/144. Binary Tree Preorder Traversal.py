# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        Given a binary tree, return the preorder traversal of its nodes' values.
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        stack_nodes = [root]
        while len(stack_nodes) > 0:
            node = stack_nodes.pop()
            result.append(node.val)
            if node.right:
                stack_nodes.append(node.right)
            if node.left:
                stack_nodes.append(node.left)
                
        return result
