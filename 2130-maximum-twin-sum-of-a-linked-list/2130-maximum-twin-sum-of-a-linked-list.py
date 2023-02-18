# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        1,first get the middle
        2,reverse the value after middle
        3,compare the value adding 
        """

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        maxSum=0
        curr1=head
        curr2=prev
        while curr2:
            maxSum = max(maxSum, (curr1.val + curr2.val))
            curr1,curr2=curr1.next,curr2.next
        return maxSum   
            
      
        