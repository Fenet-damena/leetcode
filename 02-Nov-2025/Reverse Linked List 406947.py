# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur is not None:
            new = cur.next

            cur.next = prev
            prev = cur

            cur =new
        return prev

       