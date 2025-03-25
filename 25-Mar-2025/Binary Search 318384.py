# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
            p=-1
            l,u=0,len(nums)-1
            while(l<=u):
                m=(l+u)//2
                if nums[m]==target:
                    p=m
                    break
                elif nums[m]<target:
                    l=m+1
                else:
                    u=m-1
            return p
            


        