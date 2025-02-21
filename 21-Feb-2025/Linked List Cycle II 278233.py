# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                 break
        else: 
            return None 
        while head != slow:
            head = head.next
            slow = slow.next
        return head