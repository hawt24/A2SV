class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo=[]
        dic=defaultdict(int)
        for i in  arr:
            memo.append(dic[i-difference]+1)
            dic[i]=memo[-1]
            
        return max(memo)
        

                
                
        
            
            