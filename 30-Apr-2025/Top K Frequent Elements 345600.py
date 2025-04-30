# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       heap = []

       counter = Counter(nums)

       for key , v in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (v, key))
        else:
            heapq.heappushpop(heap, (v,key))
       return [ ans[1] for ans in heap] 


        