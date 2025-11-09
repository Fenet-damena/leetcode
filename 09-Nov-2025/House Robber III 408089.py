# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def f(n):
            if not n: return (0,0)
            l, r = f(n.left), f(n.right)
            return (n.val + l[1] + r[1], max(l) + max(r))
        return max(f(root))
