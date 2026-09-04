# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Main problem : Once we reach at the end of the list, how to move backwards
        # Simple soltuion is to reverse the second half for moving towards the back

        # First reverse the second half of the linked list
        # Instead of finding the length of LL first and moving to second half by iterating
        # you can use the slow and the fast pointer to reverse the LL in one pass

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        curr = slow.next
        prev = None
        slow.next = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Prev is our current head always, not curr because it is None
        head2 = prev



        # Now start moving the Head from starting and the new Head of the second 
        # half from behind

        while head2 != None:
            temp1 = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp1
            head2 = temp2
            head = temp1
        

        




      




        