# Problem: Partition List - https://leetcode.com/problems/partition-list/

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)

        less = less_head
        greater = greater_head
        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                greater.next = cur
                greater = greater.next
            cur = cur.next

        greater.next = None  
        less.next = greater_head.next 

        return less_head.next 