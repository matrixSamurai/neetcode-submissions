# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None:
            return None

        count = 0
        slow = head
        fast = head

        while count < n:
            fast = fast.next
            count += 1
        
        if fast == None:
            head = head.next
            return head

        prev = slow
        
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
    
        prev.next = prev.next.next

        return head
        
