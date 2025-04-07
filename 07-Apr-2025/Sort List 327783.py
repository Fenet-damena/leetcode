# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getmid(head):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

def merge(left, right):
    dummy = ListNode(0)
    temp = dummy

    while left and right:
        if left.val < right.val:
            temp.next = left
            left = left.next
        else:
            temp.next = right
            right = right.next
        temp = temp.next
    if right:
        temp.next = right
    if left:
        temp.next = left
    return dummy.next



        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not  head.next:
            return head
        
        left = head
        right = getmid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left,right)


       