class Solution:
    def isPalindrome(self, s: str) -> bool:

        #remove whitespaces and make all chars lowercase
        s = s.lower()

        #initialize index
        i1 = 0 
        i2 = len(s) - 1

        print(s)

        if len(s) == 0:
            return True

        while i1 < i2:
        #check if index 1 == index 2, if it is not then immediately return False
            if s[i1].isalnum() == False:
                i1 += 1
                continue
            if s[i2].isalnum() == False:
                i2 -= 1
                continue
            
            if s[i1].isalnum() and s[i2].isalnum():

                if s[i1] != s[i2]:
                    return False

                #move the pointers inwards

                i1 += 1
                i2 -= 1

        return True



            




            

            

        
