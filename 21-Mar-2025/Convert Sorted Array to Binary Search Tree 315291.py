# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        midd = len(nums)//2
        root = TreeNode(nums[midd])

        root.left = self.sortedArrayToBST(nums[:midd])
        root.right = self.sortedArrayToBST(nums[midd+1:])
        return root





        