# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.pr=[]
        c=0
        for i in nums:
            c+=i
            self.pr.append(c)
        

    def sumRange(self, left: int, right: int) -> int:
        r=self.pr[right]
        l=self.pr[left-1]if left !=0 else 0
        return r-l
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)