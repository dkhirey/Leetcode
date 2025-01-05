# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This is a simple solution with two pointers
        # fast and slow pointers
        # fast pointer moves 2 steps and slow pointer moves 1 step
        # when fast pointer reaches end, slow pointer will be at middle
        # Intialize both pointers to head 
        fast = head
        slow = head
        # loop until fast pointer reaches end
        while fast is not None and fast.next is not None:
            # set fast pointer to move 2 steps and slow pointer to move 1 step
            fast = fast.next.next
            slow = slow.next
        # return slow pointer as it will be at middle
        return slow
    
# This is a simple solution with O(n) runtime complexity

# give me alternate approach to solve this problem
# I can think of using dictionary to store all the nodes
# and then return the middle node
# but that would be O(n) space complexity

