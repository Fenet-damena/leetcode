# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

import heapq
from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []

        for row,limit in zip(grid,limits):
            toplimi = heapq.nlargest(limit, row)
            heap.extend(toplimi)
        topk = heapq.nlargest(k, heap)
        return sum(topk)
        