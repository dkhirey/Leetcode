class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # for loop is O(n)
        # for i in range(0,n):
        #     #lookup is another O(n)
        #     if i not in nums:
        #         return i
        # return n
        # #with list total runtime is O(n^2) 1306ms
        
        ## lets use set, as it would be faster for lookup O(1)

        # here creating set of range, creating set of nums \
        # would not work because it might contain numbers other than range
        snum = set(nums)
        # for is again O(n)
        for i in range(0,n):
            #BUT lookup is O(1)
            if i not in snum:
                return i
        return n
        # overall runtime is O(n) 2ms - much more efficient :)
        # BOTTOMLINE - Set is efficient for lookups
        
        ## ChatGPT says-
        ##Sets in Python are implemented using hash tables. \
        # Each element is hashed to an index in an array, \
        # allowing for average 𝑂(1) time complexity for lookups. \
        # In contrast, lists require an 𝑂(𝑛) linear search.