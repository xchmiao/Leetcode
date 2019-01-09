
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root:
            current_level_nodes = [root]
            all_result = []
            
            while len(current_level_nodes) > 0:
                next_level_nodes = []
                level_val = []
                for node in current_level_nodes:
                    level_val.append(node.val)
                    if node.left:
                        next_level_nodes.append(node.left)
                    if node.right:
                        next_level_nodes.append(node.right)
                all_result.append(level_val)
                current_level_nodes = next_level_nodes
            return all_result
        else:
            return []
