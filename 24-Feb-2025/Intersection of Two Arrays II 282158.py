# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        point1 = 0
        point2 = 0

        nums1.sort()
        nums2.sort()
        
        ans = []
        while point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] == nums2[point2]:
                
                ans.append(nums1[point1])
                point2 +=1
                point1 +=1
            elif nums1[point1] > nums2[point2]:
                point2 +=1
            else:
                point1 +=1
        return ans
        