class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined_str = ''.join(char.lower() for char in s if char.isalnum() )

        pointer2 = len(joined_str) -1
        midpoint = len(joined_str) //2 

        for i in range(midpoint):
            if joined_str[i] == joined_str[pointer2]:
                pointer2 -= 1
            else:
                return False
        return True
            
            



        