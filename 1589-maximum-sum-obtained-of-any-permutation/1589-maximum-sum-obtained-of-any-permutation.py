class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        freq=[0]*len(nums)
        for start,end in requests:
            freq[start]+=1
            if end+1<len(nums):
                freq[end+1]-=1
        for i in range(1,len(nums)):
            freq[i]+=freq[i-1]
        temp=[]
        for i in range(len(freq)):
            temp.append((freq[i],i))
        temp.sort()
        i = 0
        for item in temp:
            freq[item[1]]=nums[i]
            i += 1
        result = 0
        preSum = [0]
        for i in freq:
            preSum.append(preSum[-1] + i)
        preSum = preSum[1:]
        for start, end in requests:
            result += preSum[end]
            if start - 1 > -1:
                result -= preSum[start - 1]
        
        return result % (10 ** 9 + 7)
            
            