# Problem: Intersection of two linked lists - https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ha = headA
        hb = headB
        if not headA or not headB:
            return None

        c1 =0
        while ha:
            c1 += 1
            ha = ha.next
        c2 = 0
        while hb:
            c2 += 1
            hb = hb.next
        ha, hb = headA, headB

        d = abs(c1-c2)
        if c1 > c2:
            for _ in range(d):
                ha = ha.next
        else:
            for _ in range(d):
                hb = hb.next
        while hb and ha:
            if ha== hb:
                return ha
            ha = ha.next
            hb = hb.next
        return None

        

        
        

        
        


 
        