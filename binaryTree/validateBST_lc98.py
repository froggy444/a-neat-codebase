# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float("-inf"), float("inf"))
    
    def isValidBSTHelper(self,node, minValue, maxValue):
        if node is None:
            return True
        if node.val < minValue and node.val >= maxValue:
            return False
        isLeftValid = self.isValidBSTHelper(node.left, minValue, node.val)
        return isLeftValid and self.isValidBSTHelper(node.right, node.val, maxValue)
            
        O(N) Time and O(h) space 