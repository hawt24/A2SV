# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # brutforce approch
        #         valA=[]
        #         valB=[]
        #         currA=headA
        #         while currA:
        #             valA.append(currA)
        #             currA=currA.next
        #         currB=headB
        #         while currB:
        #             valB.append(currB)
        #             currB=currB.next
        #         for i in range(len(valA)):
        #             for j in range(len(valB)):
        #                 if valA[i]==valB[j]:
        #                     return valA[i]
        #         return None
        currA=headA
        lenA=0
        while currA:
            lenA+=1
            currA=currA.next
        currB=headB
        lenB=0
        while currB:
            lenB+=1
            currB=currB.next
        ptrA=0
        ptrA= headA
        ptrB = headB
        if lenB>lenA:
            for i in range(lenB - lenA):
                ptrB = ptrB.next
        else:
            for i in range(lenA - lenB):
                ptrA = ptrA.next
            
        while ptrA and ptrB:
            if ptrA==ptrB:
                return ptrB
            ptrA=ptrA.next
            ptrB=ptrB.next
            
        return None
            
        
        
        

    
            

            
            