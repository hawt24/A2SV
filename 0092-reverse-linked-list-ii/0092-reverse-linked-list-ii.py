# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        creat a dummy node then go to until get before left.val then start reverse to ending           of right
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        start = prev.next
        end = start.next
        for i in range(right - left):
            start.next = end.next
            end.next = prev.next
            prev.next = end
            end = start.next
        return dummy.next
        
    
      
        
            
            
                
                
                
                
                
            
        