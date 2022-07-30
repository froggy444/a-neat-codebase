# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 
        
        if not head:
            return 
        
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 
        return prev 
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next 
        
        first_half, second_half = head , self.reverseList(slow)
        
        while second_half and first_half:
            if first_half.val != second_half.val:
                return False
            second_half = second_half.next
            first_half = first_half.next
        return True
                
        
        