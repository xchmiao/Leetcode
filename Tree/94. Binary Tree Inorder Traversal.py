
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        Given a binary tree, return the inorder traversal of its nodes' values.
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            result = []
            stack_nodes = [] # start with an empty stack
            node = root # set current node to the root
            while(len(stack_nodes) > 0 or node): 
                if node: # if the node is not empty, push it to the stack and set node -> node.left till node is empty
                    stack_nodes.append(node)
                    node = node.left
                else:
                    node = stack_nodes.pop() # then get a node from the stack, and visit its value, then set the node -> node.right
                    result.append(node.val)  # keep repeating the process till the stack is empty and the node is null
                    node = node.right
            return result
                
