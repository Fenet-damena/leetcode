# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        per = None
        curr = head
        
        while curr:
            node = curr.next  
            curr.next = per       
            per = curr            
            curr = node      
        
        return per