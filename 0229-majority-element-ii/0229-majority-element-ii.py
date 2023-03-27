class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''        if len(nums)==len(set(nums)) and len(nums)<=2:
            return nums
        
        cnt=Counter(nums)
        ans=[]
        for i in range(len(nums)):
            print(cnt[nums[i]])
            if cnt[nums[i]]>len(nums)//3:
                ans.append(nums[i])
        return list(set(ans))
        '''
        cnt = Counter(nums)
        ans = []
        for key, val in cnt.items():
            if val >len(nums) // 3:
                ans.append(key)
        return ans



        