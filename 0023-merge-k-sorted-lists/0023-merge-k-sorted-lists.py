# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        sorted_arr=[]
        for i in lists:
            curr=i
            while curr:
                heappush(heap,curr.val)
                curr=curr.next
        while heap:
            sorted_arr.append(heappop(heap))
            
        ans=ListNode()
        dummy=ans
        for i in sorted_arr:
            ans.next=ListNode(i)
            ans=ans.next
        return dummy.next
            
        
                
                
        
                
   
   
        
        
        
        
        
        
        
        