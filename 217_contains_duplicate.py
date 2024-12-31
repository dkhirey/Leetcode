class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash = {}
        hash = set()
        for num in nums:
            if num in hash:
                return True
            else:
                # hash[num] = 1
                hash.add(num)
        return False
        