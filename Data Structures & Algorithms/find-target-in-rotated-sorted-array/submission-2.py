class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #set left and right pointer
        left = 0
        right = len(nums) -1

        #while loop to loop through the array, loop exits when left == right > found the midpoint
        while left < right:
            #set midpoint
            mid = (left + right) // 2

            #if the number at mid is greater than the number at right, the breakpoint must be to the right
            if(nums[mid] > nums[right]):
                #increment left, add 1 to avoid infinite loop when left = 0 and right = 1
                left = mid + 1

            #if the number at mid is less than the number at right, the breakpoint must be to the left
            elif(nums[mid] < nums[right]):
                right = mid

    ######### LOOP 2 ###############
        rotation_point = right

        if(nums[0] <= target <= nums[rotation_point -1 ]):
                # search on the left
                left_2 = 0
                right_2 = rotation_point - 1

                while left_2 <= right_2:
                    mid_2 = (left_2 + right_2) // 2
                    
                    if(target == nums[mid_2]):
                        return mid_2
                    elif(target < nums[mid_2]):
                        right_2 = mid_2 - 1
                    elif(target > nums[mid_2]):
                        left_2 = mid_2 + 1
                    

        if(nums[rotation_point] <= target <= nums[-1]):
            #search on the right

            left_2 = rotation_point
            right_2 = len(nums) -1

            while left_2 <= right_2:
                mid_2 = (left_2 + right_2) // 2
                
                if(target == nums[mid_2]):
                    return mid_2
                elif(target < nums[mid_2]):
                    right_2 = mid_2 - 1
                elif(target > nums[mid_2]):
                    left_2 = mid_2 + 1
        
        return -1
        



        
        


            
        