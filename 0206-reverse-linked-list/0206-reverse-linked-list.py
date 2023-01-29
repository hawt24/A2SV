# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr_num=None,head
        while curr_num:
            nextt=curr_num.next
            curr_num.next=prev
            prev=curr_num
            curr_num=nextt
        return prev
        