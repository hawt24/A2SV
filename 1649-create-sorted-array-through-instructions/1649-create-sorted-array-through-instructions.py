from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        temp=SortedList([])
        ans=0
        for i in range(len(instructions)):
            
            num=instructions[i]
            
            idx_left=temp.bisect_left(num)
            idx_right=temp.bisect_right(num)
            
            ans+=min(idx_left,len(temp)-idx_right)
            
            temp.add(num)
            
        return ans % (10**9 + 7)
   
        
        