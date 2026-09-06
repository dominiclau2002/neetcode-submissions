class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first sort the array

        #convert everything to a hashmap to get the index of each number
        map = {}

        # {3:0,4:1,5:2,6:3}

        #initialize index counter 
        index = 0 
        for n in nums:

            diff = target - n
            #look up index of the difference if it exists
            if diff in map:
                return [map[diff],index]

            map[n] = index
            index += 1

        return [0,0]

            




        



        