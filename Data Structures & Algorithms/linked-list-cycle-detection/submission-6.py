# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycleNonIntelligent(self, head: Optional[ListNode]) -> bool:

        # Solving using the set
        visited = set()

        while head != None:

            if head in visited:
                return True
            
            visited.add(head)
            
            head = head.next
        
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while slow and fast and slow.next != None and fast.next != None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
