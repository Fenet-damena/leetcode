# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def dfs(node):
            nonlocal arr
            if node:
                dfs(node.left)
                arr.append(node.val)
                dfs(node.right)
            

        def addNode(i, j):
            if i == j:
                return None
            mid = (i+j) // 2
            node = TreeNode(arr[mid])
            node.left = addNode(i, mid)
            node.right = addNode(mid+1, j)
            return node
        dfs(root)
        return addNode(0, len(arr))        