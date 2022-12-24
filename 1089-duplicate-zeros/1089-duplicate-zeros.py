class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        start=0
        while start<len(arr)-1:
            if arr[start]==0:
                arr.insert(start+1,0)
                start+=1
                arr.pop()
            start+=1
       # arr[:start]=arr[:len(arr)-1]
            
            
                
                