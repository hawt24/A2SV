class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        temp = []
    
        heapq.heapify(temp)
        
        for i in range(min(k,len(nums1))):
            for j in range(min(k,len(nums2))):
                
                pairs = [nums1[i],nums2[j]]
                if len(temp)<k:
                    heapq.heappush(temp,[-(nums1[i]+nums2[j]),pairs])
                else:
                    if nums1[i]+nums2[j]>-temp[0][0]:
                        break
                    heapq.heappush(temp,[-(nums1[i]+nums2[j]),pairs])
                    heapq.heappop(temp)
        
        ans = []
        for i in range(len(temp)):
            ans.append(temp[i][1])
        
        return ans