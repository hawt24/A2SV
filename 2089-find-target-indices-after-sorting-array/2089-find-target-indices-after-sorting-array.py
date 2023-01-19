class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for idx,val in enumerate(sorted(nums)):
            if val==target:
                ans.append(idx)
        return ans