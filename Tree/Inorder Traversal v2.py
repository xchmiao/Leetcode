"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

## use dummynode
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):

    	if not root:
    		return []

    	dummynode = TreeNode(0)
    	dummynode.right = root
    	stack = [dummynode]
    	result = []

    	while stack:
    		node = stack.pop()
    		if node.right:
    			node = node.right
    			while node:
    				stack.append(node)
    				node = node.left

    		if stack:
    			result.append(stack[-1].val)

    	return result


# from leetcode tutorial
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):

    	if not root:
    		return []


    	stack = []
    	result = []
    	node = root

    	while node or stack:
    		if node:
    			stack.append(node)
    			node = node.left
    		else:
    			node = stack.pop()
    			result.append(node.val)
    			node = node.right

    	return node
