# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in matrix:
            for j in i:
                heapq.heappush(heap,j)
        x = 0
        for i in range(k):
            x = heapq.heappop(heap)
        return x

        