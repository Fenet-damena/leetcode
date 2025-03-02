# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_count = 0
        temp_head = ListNode()
        temp_current = temp_head 
        prev_node = None
        max_sum = 0
        current = head
        
        while current:
            new_node = ListNode(current.val)
            temp_current.next = new_node
            temp_current = new_node
            current = current.next
    
        current = head 
        while current:
            node_count += 1
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        
        node_count = node_count // 2
        current = temp_head.next
        
        while node_count > 0:
            max_sum = max(max_sum, current.val + prev_node.val)
            current = current.next
            prev_node = prev_node.next
            node_count -= 1

        return max_sum
