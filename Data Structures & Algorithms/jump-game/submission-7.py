class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_index = len(nums) - 1

        if(len(nums) == 1):
            return True

        for i in range(goal_index,-1,-1):

            if(i + nums[i]) >= goal_index:
                goal_index = i
            
        if(goal_index != 0):
            return False
        else:
            return True



        
        
