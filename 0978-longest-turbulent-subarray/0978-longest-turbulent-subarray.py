class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        It is smaller than previous and smaller than next
						Or
	    It is bigger than previous and bigger than next
        means
        a > b < c > d < e
        arr[right-1]< arr[right]> arr[right+1]
		a < b > c < d > e
        arr[right-1] >arr[right]< arr[right+1]
        """
        ans=0
        left=0
        right=0
        while right<len(arr):
            while right<len(arr)-1 and (arr[right-1]>arr[right]<arr[right+1] or arr[right-1]<arr[right]>arr[right+1]):
                right+=1
            while left<right and arr[left]==arr[left+1]:#for hundlign duplicate
                left+=1
            ans=max(ans,right-left+1)
            left=right
            right+=1
        return ans
    
    
            
            
                
            
      