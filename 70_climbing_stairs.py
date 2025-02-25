class Solution:
    def climbStairs(self, n: int) -> int:
        # if there is only 1 step there is only 1 way
        if n == 1 : return 1
        # initiate array to memoize 
        ways = [0]*n

        ways[0] = 1 # first step only 1 way
        ways[1] = 2 # second step 2 ways - 1+1 or 2

        # run loop for rest of steps
        for i in range(2, len(ways)):
            # number of ways are ways to previous step which is 1 step away\
            # plus ways to previous to previous step which is 2 steps away 
            ways[i] = ways[i-1] + ways[i-2]
        # return last element of array as we reach to top of stairs
        return ways[-1]

    ### similar to fibonacci top down DP approach
    # time complexity O(n)
    
### Alternate approach - traversing in reverse direction
class Solution:
    # time complexity O(n)
    # space complexity O(1)
    # for example if n = 5 then ways = [1,2,3,5,8]
    # ways[0] = 1
    def climbStairs(self, n: int) -> int:
        # if there is only 1 step there is only 1 way
        last, butone = 1,1        
        # for i in range(n-1):
        #     butone, last = last, last + butone
        for i in range(-3,-1,-1):
            # loop runs for n-3 times as we are starting from 3rd last element
            # and goes upto 1st element 
            # butone is last element and last is sum of last and butone
            temp = last
            last = last + butone
            butone = temp
            # return last element as we reach to top of stairs
        return last