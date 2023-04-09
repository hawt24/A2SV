class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        """the bruteforce approch but the prouct of arr is very high number"""
        # product=1
        # for num in nums:
        #     product*=num
        # arr=[]
        # d=2
        # while d*d<=product:
        #     while product%d==0:
        #         arr.append(d)
        #         product//d
        #     d+=1
        # if n>1:
        #     arr.append(n)
        """then we can express in prime factrose the return the set elelment of arr"""
        ans=[]
        for i in range(len(nums)):
            #when cheak prime number we can sure up to the squre root number 
            sqrt=int(math.sqrt(nums[i]))
            for num in range(2,sqrt+1):
                if nums[i]%num==0:
                    ans.append(num)
                    while nums[i]%num==0:
                        nums[i]=nums[i]//num
            if nums[i]>=2:
                ans.append(nums[i])
        return len(set(ans))
                        
            
        
        
            
                