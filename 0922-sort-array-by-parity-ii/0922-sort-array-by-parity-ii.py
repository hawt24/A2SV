class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        ans= []
        for i in range(len(even)):
            ans+= [even[i],odd[i]]
            
        return ans
        