# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        1,2,3,4 
        
        prev, curr = None, head 
        
        if not head:
            return 
        
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp 
        return prev 
    

    iteration 1 
    prev = none -> 1 # remember prev is returned only once after while loop and is the head of reversed list  
    current = 1 ->2 
    temp = 2
    current.next = None 

    iteration 2 
     prev = 1 -> 2  # remember prev is returned only once after while loop and is the head of reversed list  
    current =2 ->3 
    temp = 3
    current.next = 3 

    iteration 3 
    temp = 4
    curr.next = 4
    prev = 3
    curr = 4

    iteration 4
    temp = None 
    curr.next = 3
    prev = 4 
    curr = 4


    
    
    
        
        
        