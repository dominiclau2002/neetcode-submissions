class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #initialize the current sum of all the numbers we are taking in
        current_sum = 0
        max_sum = None
        indexer = 0

        for i in range(len(nums)):

            #check whether adding the current number at i into the current_sum will 
            #result in the highest possible sum
            if(current_sum + nums[i] >= nums[i]):
                #add the number into the sum
                current_sum += nums[i]
                if max_sum is None or current_sum > max_sum:
                    max_sum = current_sum
        
            else: #if adding the number into the current_sum will decrease the current_sum
            #drop the current sum and start fresh
                current_sum = nums[i]
                if  max_sum is None or current_sum > max_sum:
                    max_sum = current_sum
         

        return max_sum



        