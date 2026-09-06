class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined_str = ''.join(char.lower() for char in s if char.isalnum() )
        print(joined_str)

        pointer1 = 0
        pointer2 = -1

        for i in range(0,(len(joined_str)//2)):
            if joined_str[i] == joined_str[pointer2]:
                pointer2 -= 1
            else:
                return False
        return True
            
            



        