# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        first creat 2 node the firts carry less than x numbwr and the second node carry 
        greater than x then connect two node
        """
        less_x=ListNode()
        greater_x=ListNode()
        left=less_x
        right=greater_x
        curr=head
        while curr:
            if curr.val<x:
                left.next=curr
                left=left.next
            else:
                right.next=curr
                right=right.next
            curr=curr.next
        left.next=greater_x.next
        right.next=None
        return less_x.next
  
                