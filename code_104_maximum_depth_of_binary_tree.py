from dataclasses import dataclass
from turtle import right
# Definition for a binary tree node.
@dataclass
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        path = self.longest_path(root)
        return len(path)

    def longest_path(self, root: TreeNode):
        if not root:
            return []
        
        right_vector = self.longest_path(root.right)
        left_vector = self.longest_path(root.left)
        
        if len(left_vector) > len(right_vector):
            left_vector.append(root.val)
        else:
            right_vector.append(root.val)

        if len(left_vector) > len(right_vector):
            return left_vector
        
        return right_vector