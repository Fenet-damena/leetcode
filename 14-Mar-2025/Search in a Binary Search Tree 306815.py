# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def binry(node,val):

            if not node:
                return node
            if val == node.val:
                return node
            elif val > node.val:
                return binry(node.right,val)
            else:
                return binry(node.left,val)
        return binry(root,val)

            


            

        