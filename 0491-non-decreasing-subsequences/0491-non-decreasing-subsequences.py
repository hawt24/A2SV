class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        def backtrack(path,idx):
            nonlocal ans
            if len(path)>1:
                ans.append(path[::])
            
            used=[]
            
            for i in range(idx, len(nums)):
                
                if nums[i] in used:
                    continue
                    
                if not path or nums[i]>=path[-1]:
                    used.append(nums[i])
                    path.append(nums[i])

                    backtrack(path,i+1)
                    path.pop()
                    
        backtrack([],0)
        return ans
    
                    
                    