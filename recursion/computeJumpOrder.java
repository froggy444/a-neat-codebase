class ListNode {
    int value;
    ListNode jump;
    Listode next

    public ListNode(){
        this.value = -1; // unexplored node are set to -1 so we can give a sequence value as we visit, in the end print values of linkedlist from head for output
        this.jump = jump;
        this.next = next;
    }
}

public class JumpListTraversal{

    private ListNode prepareNodes(){
        //create the empty nodes 
        ListNode head = new ListNode();   // Our example has 5 nodes so we are creating 5 nodes here, for another input we need to modify this and connections
        ListNode node2= new ListNode();
        ListNode node3= new ListNode();
        ListNode node4= new ListNode();
        ListNode node5= new ListNode();

        // add jump connections 

        head.jump = node3;
        node2.jump = node4;
        node3.jump = node2;
        node4.jump = null;
        
        //add next connections
        head.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;

    public void computeJumpOder(ListNode head){ // only head is passed as we just first node of the LinkedList rest can be derived through pointers
        Integer orderCounter = 1; // external variable to increment and keep the next value ready that needs to be put in the node that will traversed next
        computeJumpOrderHelper(head, orderCounter);
    }
    // this is the recursive version 
    private void computeJumpOrderHelper( ListNode node, Integer orderCounter){
        if(node == null || node.value != 1){ //this is the base case that will break recursion, and we have to check for null as the node for end of linkedlist,
        // or node.value is not -1 because we want to only visit the unvisited nodes 
            return;
        }

        //do the work on the node - we have two things here when we visit it, make its value as orderCounter and increment value of orderCounter to keep next value ready in it
        node.value = orderCounter; // set the value
        orderCounter++; // keep next value ready

        // explore pointers
        computerJumpOrderHelper(node.jump, orderCounter); // first all of the jump tree will be executed recursively
        computeJumpOrderHelper(node.next, orderCounter);
    }


   
    }
    public void printList(ListNode head){
        ListNode temp = head;
        while(temp != null){
            System.out.println(temp.value);
            temp = temp.next;
        }
    public static void main(String[] args){
        JumpListTraversal traverse = new JumpListTraversal();
        ListNode head = traverse.prepareNodes();

        //compute using recursive or iterative function
        traverse.computeJumpOder(head);
        //traverse.computeJumpOrderIterative(head);
        traverse.printList()
    }

}



