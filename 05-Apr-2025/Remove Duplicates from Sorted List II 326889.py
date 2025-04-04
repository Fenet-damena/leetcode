# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

      
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.val == cur.next.val:
                    cur = cur.next 
                prev# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

      
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next 
                prev.next = cur.next
               
            else:
                
                prev = prev.next
            cur = cur.next
        return dummy.next
        
               
  