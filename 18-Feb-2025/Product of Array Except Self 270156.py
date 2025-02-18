# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*len(nums)
        p1=1
        for i in range(len(nums)):
            a[i]=p1
            p1*=nums[i]
        p2=1
        for j in range(len(nums)-1,-1,-1):
            a[j]*=p2
            p2*=nums[j]
        return a

        