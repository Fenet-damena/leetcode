# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float('inf')
        global_ans = float("inf")
        for i  in range(len(nums)-2):
            s=target-nums[i]
            r=len(nums)-1
            l=i+1
            while l<r:
                d=nums[i] + nums[l]+nums[r]
                if abs(target - d ) < abs(target - ans):
                    ans = d
                if d == target:
                    break
                elif d < target:
                    l+=1
                else:
                    r-=1
        return ans

                



       
      