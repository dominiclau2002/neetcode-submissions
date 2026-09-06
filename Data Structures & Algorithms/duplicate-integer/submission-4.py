class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        l = len(nums)
        s = set(nums)
        lengthset = len(s)
        if l > lengthset:
            return True

        return False

        