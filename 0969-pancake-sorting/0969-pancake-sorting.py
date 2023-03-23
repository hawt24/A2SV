class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
         
        def flip(arr, k):
            arr[:k+1] = reversed(arr[:k+1])
                
        
        length = len(arr)
        result = []
        m = length-1
        for _ in range(length):
            max_idx = 0
            for j in range(m+1):
                if arr[j] > arr[max_idx]:
                    max_idx = j
                    
            if max_idx == m:
                m -= 1
                continue
                
            if max_idx != 0:     
                flip(arr, max_idx)
                result.append(max_idx+1)
				
            flip(arr, m)             
            result.append(m+1)
            m -= 1
            
        return result
