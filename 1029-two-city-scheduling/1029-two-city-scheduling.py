class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        sorted_arr=sorted(costs,key=lambda x:x[0]-x[1])
        n=len(sorted_arr)//2
        ans=0
        for i in range(n):
            ans+=sorted_arr[i][0]+sorted_arr[i+n][1]
            
        return ans
            