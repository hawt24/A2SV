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
        def dfs(id):
            ans=dic1[id]
            for sub in dic2[id]:
                ans+=dfs(sub)
            return ans
                
        dic1={}
        dic2={}
        
        for employee in employees:
            dic1[employee.id]=employee.importance
            dic2[employee.id]=employee.subordinates
            
        return dfs(id)
        