# Link: https://leetcode.com/problems/remove-linked-list-elements/
class Solution:
    # This approach is simple and efficient
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a new linked list with a dummy node
        newll = ListNode(0)
        # Point the next node of the dummy node to the head
        newll.next = head
        
        # Innitialize pointers to the head of the linked list
        current = head
        # Initialize previous pointer to the dummy node
        previous = newll
        # Traverse the linked list and remove the nodes with the given value
        while current:
            # If the value of the current node is equal to the given value
            if current.val == val:
                # Remove the node by pointing the next node of the previous node to the next node of the current node
                previous.next = current.next
            # If the value of the current node is not equal to the given value
            else:
                # Move the previous pointer to the current node
                previous = current
            # Move the current pointer to the next node in the linked list
            current = current.next     
        # Return the next node of the dummy node which is the head of the new linked list           
        return newll.next
    
    # Time complexity: O(n) - We traverse the linked list once
    # Space complexity: O(1) - We use constant space
    
    # other approach is to use recursion to remove the elements 
    # but that would be O(n) space complexity as it uses recursion stack
    
    # Another approach is to use a stack to store the nodes to be removed
    # and then remove the nodes after traversing the linked list
    # but that would be O(n) space complexity as it uses stack
    
    