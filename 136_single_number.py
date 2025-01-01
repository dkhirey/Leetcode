class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # maintain a dictinary to keep count
        sdict = {}
        for num in nums:
            # if its first time set the counter to 1 else increase counter
            if num not in sdict.keys():
                sdict[num] = 1
            else :
                sdict[num] += 1
        # go over the dictionary to find which one appears only once
        for k in sdict.keys():
            if sdict[k] == 1:
                return k
        return None

### This is a very straight forward solution
# Time complexity is O(n) - to go over nums + to go over dictionary
# space complexity can be improved as dictionary has to be maintained
        