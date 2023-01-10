class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans=0
        dic={}
        for x in deliciousness:
            for i in range(22):
                y=2**i-x
                if y in dic:
                    ans+=dic[y]
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        return ans%(10**9+7)
      
            
            
        