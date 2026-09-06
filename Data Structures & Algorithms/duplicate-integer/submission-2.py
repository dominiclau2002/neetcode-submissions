class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #sort array first
        nums.sort()

        #create a stack
        s = []
        
        #iterate through the list
        for i in nums:

            #check if the number is already in the stack
            if i not in s:
            #put the number into the stack
                s.append(i)
            
            #if a number is already in the stack -> duplicate
            else:
                return True

        return False

            


            

        