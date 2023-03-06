# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        def helper(list1,list2,curr):
            if not list1 or not list2:
              curr.next=list1 or list2
              return
            if list1.val < list2.val:    
                curr.next=list1
                helper(list1.next,list2,curr.next)
            else:
                curr.next=list2
                helper(list1,list2.next,curr.next)
            return
        helper(list1,list2,curr)
        return dummy.next