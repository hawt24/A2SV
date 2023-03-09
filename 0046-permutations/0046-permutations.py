class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        
        def backtrack(path):
            
            if len(path) == len(nums):
                ans.append(path)
                return 
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    backtrack(path + [nums[i]])
                    used.remove(nums[i])
                
                
        ans=[]
        backtrack([])
        return ans
                
                