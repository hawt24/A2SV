class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # used = set()
        
        # def backtrack(path):
            
            # if len(path) == len(nums):
            #     ans.append(path)
            #     return 
            
            # for i in range(len(nums)):
            #     if nums[i] not in used:
            #         used.add(nums[i])
            #         backtrack(path + [nums[i]])
                    # used.remove(nums[i])
                
        # ans=[]
        # backtrack([])
        # return ans
        ans = []

        def backtrack(temp = [],s = 0):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            for i in range(len(nums)):
                if s & (1 << i) == 0:
                    temp.append(nums[i])
                    s |= 1 << i
                    backtrack(temp,s)
                    s &= ~(1 << i)
                    temp.pop()
        backtrack()
        return ans
                
        