# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Solution-1
'''
1.1 Create an empty stack
2.1 Do following while root is not NULL
    a) Push root's right child and then root to stack.
    b) Set root as root's left child.
2.2 Pop an item from stack and set it as root.
    a) If the popped item has a right child and the right child 
       is at top of stack, then remove the right child from stack,
       push the root back and set root as root's right child.
    b) Else print root's data and set root as NULL.
2.3 Repeat steps 2.1 and 2.2 while stack is not empty.

'''
class Solution(object):
    def peekStack(self, stack):
        if len(stack) > 0:
            return stack[-1]
        else:
            return None
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            result = []
            stack_nodes = []
            node = root
            while True:
                while node:
                    if node.right:
                        stack_nodes.append(node.right)
                    stack_nodes.append(node)
                    node = node.left   
                node = stack_nodes.pop()
                top_node = self.peekStack(stack_nodes)
                if (node.right == top_node) and (node.right is not None):
                    stack_nodes.pop()
                    stack_nodes.append(node)
                    node = node.right
                else:
                    result.append(node.val)
                    node = None
                if len(stack_nodes) == 0:
                    break
            return result
        
## Solution-2

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]
