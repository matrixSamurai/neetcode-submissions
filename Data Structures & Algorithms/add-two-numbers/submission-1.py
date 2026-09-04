# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        newHead = None
        carry = 0

        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            sum = l1val + l2val + carry

            newNode = ListNode(0, None)
            if newHead == None:
                newHead = newNode

            if sum > 9:
                rem = sum %10
                carry = 1
                newNode.val = rem
            else:
                newNode.val = sum
                carry = 0
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if prev != None:
                prev.next = newNode

            prev = newNode
               
         


        if carry != 0:
            # Attach this as 1
            prev.next = ListNode(1, None)

        
        return newHead
            

