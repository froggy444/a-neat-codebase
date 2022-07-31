# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #this ensures the next node to dummy is head
        left = dummy
        right = head #while because right needs to be initialized to head + n and since its linkedlist we cannot do it directly
        # take right n times ahead of left
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # now traverse with these fast and slow pointers till the fast pointer right reaches end of list, left we will at the node whose next pointer needs to be connected to the next nodes next pointer left will be at 3 if 4 needs to be removed and will be connected to 5, this is achieved by initializing left at dummy instead of head
        
        while right:
            left = left.next
            right = right.next 
        left.next = left.next.next
        
        return dummy.next #this points to original head as dummy is a sentinal node before the head in our case
        