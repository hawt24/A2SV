class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        subArr=0
        for x in range(len(nums)):
            temp=nums[x]
            for y in range(x,len(nums)):
                temp=math.lcm(temp, nums[y])
                if temp==k:
                    subArr+=1
        return subArr
                    