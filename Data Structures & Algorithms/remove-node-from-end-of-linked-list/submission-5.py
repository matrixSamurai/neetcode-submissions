# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # [1,2,3,4,5] n = 2
        #      S   F

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        ## Increment the fast pointer first
        for _ in range(n):
            fast = fast.next

        # Move both the pointers util fast pointer reaches end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next= slow.next.next

        return dummy.next

        
        

