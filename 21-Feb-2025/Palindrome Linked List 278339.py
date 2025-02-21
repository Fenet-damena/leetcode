# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lists = []
        pointer = head

        while pointer:
            lists.append(pointer.val)
            pointer = pointer.next

        pointer1 = head

        while pointer1:
            if pointer1.val == lists[-1]:
                lists.pop()
            pointer1 = pointer1.next

        if len(lists) == 0:
            return True
        return False