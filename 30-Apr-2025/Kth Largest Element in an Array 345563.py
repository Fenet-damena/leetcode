# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-n for n in nums]
        heapq.heapify(heap)

        while k > 1 :
            heapq.heappop(heap)
            k -= 1
        return -heap[0]
        
        