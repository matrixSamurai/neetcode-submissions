# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previousHead = None

        while head != None:

            nextHead = head.next
            head.next = previousHead
            previousHead = head
            head = nextHead
        
        return previousHead



        