class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we need to check that the 2 numbers at the deflection point are not in order e.g. b > a
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            #if the middle element is more than right, the breakpoint is to the right
            if(nums[mid] > nums[right]):
                left = mid + 1
            #if the middle element is less than right, the breakpoint is to the left
            elif(nums[mid] < nums[right]):
                right = mid

        return nums[right]

                

            



        
        