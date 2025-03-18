# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def inorder_successor(node):
            cur = node
            while cur.left:
                cur = cur.left
            return cur

        def delt(node, key):
            if not node:
                return node
            if node.val > key:
                node.left = delt(node.left, key)
            elif node.val < key:
                node.right = delt(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                temp = inorder_successor(node.right)
                node.val = temp.val  
                node.right = delt(node.right, temp.val)
            return node
        
        return delt(root, key)
