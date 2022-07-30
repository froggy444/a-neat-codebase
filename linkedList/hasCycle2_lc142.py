# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited= set()
        temp = head
        
        if temp is None:
            return None
        while(temp):
            if(temp in visited):
                return temp 
            else:
                visited.add(temp)
                temp = temp.next
        return None
        

# although this uses extra memory 

#sol2 with less memory usage tortoise algo modification for hasCycle regular 

class Solution:
    def intersectingPoint(self, head: Optional[ListNode]) -> bool:        
        fast = head
        slow = head
        
        while fast and fast.next and fast.next.next:
      
            slow = slow.next 
            fast = fast.next.next
	        if slow is fast:
                return slow
            
    def detectCycle(self, head):
	    if head is None:
	        return None
	
	    pointer1=self.intersectingPoint(head)
	    pointer2=head
	    while pointer1!=pointer2:
		    pointer1=pointer1.next
		    pointer2=pointer2.next
	    return pointer2
