class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}


        for index,value in enumerate(nums):
            dict[value] = index

        for index, value in enumerate(nums):
            diff = target - value
            if diff in dict and dict[diff] != index:
                return [index,dict[diff]]



