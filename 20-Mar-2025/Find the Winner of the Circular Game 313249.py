# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Linked:
    def __init__(self, val):
        self.next = None
        self.val = val

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dummy_node = Linked(1)
        curr = dummy_node
        for _ in range(2, n + 1):
            node = Linked(_)
            curr.next = node
            curr = node
        curr.next = dummy_node

        curr = dummy_node 
        temp = curr
        
        while n > 1:
            for _ in range(k - 1):
                temp = curr
                curr = curr.next

            temp.next = curr.next  
            curr = curr.next  
            n -= 1  

        return curr.val  