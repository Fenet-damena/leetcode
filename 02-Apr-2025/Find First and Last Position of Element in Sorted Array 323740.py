# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums , target , biasleft):
            ans = -1
            low , high = 0, len(nums)-1
            
            while low <= high:
                mid = (low + high)//2
                if nums[mid] > target:
                    high  = mid -1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    ans = mid
                    if  biasleft:
                        high = mid -1
                    else:
                        low = mid + 1
            return ans
        left = search(nums, target, True)
        right = search(nums,target,False)
        return [left, right]
            

        