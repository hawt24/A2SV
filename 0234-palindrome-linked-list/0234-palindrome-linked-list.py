# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
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
        while prev and head:
            if prev.val!=head.val:
                return False
            head=head.next
            prev=prev.next
        return True
    
        
            