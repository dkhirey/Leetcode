class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## intitiating variables for local and global max
        ## starting alues with first element as 
        # it will take care of edge case where n = 1
        seqsum = nums[0]
        mxsum = nums[0]
        # print(nums)
        ## loop over rest of the elements
        ## here lopp starts from 1 as we have already taken care of 0th element
        for i in range(1,len(nums)):
            # print(nums[i],"...",seqsum,"...",mxsum)
            ## if current element is greater than sum of sequence sum + current element
            ## this takes care of negative numbers and suquence sum
            if nums[i] >= seqsum + nums[i]:
                seqsum = nums[i]
            else:
                ## if current element is not greater than sum of sequence sum + current element
                # usual case 
                seqsum = seqsum + nums[i]
            ## set global max to maximum of sequence sum and global max
            mxsum = max(seqsum,mxsum)
        # print(mxsum)
        return mxsum
    
## simple solution with O(n) runtime complexity 66ms

#---------------------------------------------------------#
## another approach

def maxSubArray(nums):
    largest = currentsum = nums[0]
    for i in range(1,len(nums)):
        #print('num...',nums[i])
        currentsum = max(currentsum+nums[i],nums[i]) 
        #print('currentsum...',currentsum)
        largest = max(currentsum,largest)
        #print('largest...',largest)
    return largest

## This takes 98s runtime complexity O(n)