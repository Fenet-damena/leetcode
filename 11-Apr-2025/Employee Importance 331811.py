# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        empmap = {emp.id: emp for emp in employees}

        def dfs(eid: int) ->int:

            emp = empmap[eid]
            ans = emp.importance
        
            for  i in emp.subordinates:
                ans += dfs(i)
            return ans
        return dfs(id)
            

        