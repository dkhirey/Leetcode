class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## on the similar lines of two pointers solution
        ## we can use fast and slow pointers to detect cycle
        fast = head
        slow = head
        # make sure its not end of list, loop until end
        while fast is not None and fast.next is not None :
            ## fast pointer moves 2 steps and slow pointer moves 1 step
            fast = fast.next.next
            slow = slow.next
            ## if fast and slow pointers meet, there is a cycle
            if fast == slow:
                return True

        return False
    
### I like this solution, its simple and efficient. 
# Time complexity is O(n) and space complexity is O(1)
## there is other solution based on dictionary, 
# but that would be O(n) space complexity