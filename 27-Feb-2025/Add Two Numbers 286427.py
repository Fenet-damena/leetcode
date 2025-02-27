# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         def add_helper(node1, node2, carry_over):
            if not node1 and not node2 and not carry_over:
                return None
            
            total = 0
            if node1:
                total += node1.val
                node1 = node1.next
            if node2:
                total += node2.val
                node2 = node2.next

            if carry_over:
                total += 1
                carry_over = False

            if total >= 10:
                carry_over = True

            return ListNode(total % 10, next=add_helper(node1, node2, carry_over))

         return add_helper(l1, l2, False)
        