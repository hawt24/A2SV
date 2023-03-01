class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(start,end):
            if start==end:
                return nums[end]
            left=nums[start]
            right=nums[end]
            left_op=helper(start+1,end)
            right_op=helper(start,end-1)
            return max(left-left_op,right-right_op)
        temp=helper(0,len(nums)-1)
            
        return temp >= 0