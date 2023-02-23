class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start=0
        end=0
        dic=defaultdict(int)
        window_size=0
        while end<len(fruits):
            dic[fruits[end]]+=1
            while len(dic)>=3:
                dic[fruits[start]]-=1
                if dic[fruits[start]]==0:
                    del dic[fruits[start]]
                
                start+=1
            window_size=max(window_size,end-start+1) 
            end+=1
        return window_size
            
            
        

  