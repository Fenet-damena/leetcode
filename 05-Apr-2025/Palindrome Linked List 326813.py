# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            keep = slow.next
            slow.next= prev
            prev = slow
            slow = keep
        
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            