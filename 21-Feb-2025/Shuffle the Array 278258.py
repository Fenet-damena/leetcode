# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = len(nums)//2
        list1 = nums[:mid]
        list2 = nums[mid:]
        
        ans = []
        for i in range(mid):
            ans.append(list1[i])
            ans.append(list2[i])

        return ans 