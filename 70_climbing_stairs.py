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
        