# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Function to reverse the linked list
    def reverse(self, head: ListNode) -> ListNode:
        #   Initialize pointers prev to None and curr to head
        prev = None
        curr = head
        #  Traverse the list
        while curr:
            # Save the next node
            next_temp = curr.next
            # Reverse the link
            curr.next = prev
            # Move pointers forward
            prev = curr
            # Move curr to the next node
            curr = next_temp
        # prev is now the new head of the reversed list
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize slow and fast pointers to head
        slow = head
        fast = head
        # Traverse the list to find the middle node
        while fast and fast.next:
            # Move slow pointer by 1 step and fast pointer by 2 steps
            slow = slow.next
            fast = fast.next.next
        
        # After getting middle node, reverse the list after that node.    
        # Reverse the second half of the list
        rev = self.reverse(slow)
        
        # Compare the first half and the reversed second half 
        while rev:
            # If the values are not equal, return False
            if head.val != rev.val:
                return False
            # Move the pointers forward to compare the next nodes
            head = head.next
            rev = rev.next
        # If all the values are equal, return True
        return True
    
# This solution uses two pointers to find the middle of the linked list
# This is a solution with O(n) runtime complexity and O(1) space complexity
# There are other solutions to solve this problem using stack and recursion
# But this is the most efficient solution

# stack solution time complexity O(n) and space complexity O(n).
# stack solution copies all the nodes to stack and then compares the nodes by popping from stack

# recursive solution time complexity O(n) and space complexity O(n).
# recursive solution uses recursion to compare the nodes by moving the head pointer to the end and comparing the nodes while returning back