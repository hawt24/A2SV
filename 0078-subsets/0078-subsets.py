class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start,path):
            ans.append(path[::])
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        ans=[]        
        backtrack(0,[])
        return ans