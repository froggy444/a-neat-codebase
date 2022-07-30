# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
   #anytime you have something to do with head and tail or need to find the center of the list use Floyd's tortoise and hair approach 
        #finding the mid
        slow = head
        fast = head.next 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # reverse the second half
        
        second = slow.next 
        prev = slow.next = None                # slow.next ko none isiliye kiya kyu ki we want to break connection of second half of list with first half and prev isiliye none hai kyu ki har reverse kar k we going node by node to next node ka bhi aage k list se connection cut karna h badme jod dege reversed node se 
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp 
        
        # merge them 
        first, second = head, prev 
        
        while second:
            temp1 , temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1 
            first, second = temp1, temp2
            
        
        