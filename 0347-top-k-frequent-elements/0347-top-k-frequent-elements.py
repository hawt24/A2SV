class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]]+=1
        temp=dict(sorted(cnt.items(), key=lambda x: x[1], reverse=True))
        ans=list(temp.keys())[:k]
        return ans
        

   