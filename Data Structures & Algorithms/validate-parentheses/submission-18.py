class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack
        stack = []

        #define valid brackets as a hash map:
        valid = {"}":"{",")":"(","]":"["}

        if len(s) == 0 or len(s) == 1 or s[0] in "}])":
            return False

        for i in range(len(s)):
            #if it is an opening bracket:
            if s[i] in "{([":
             #add to the stack
                stack.append(s[i])
            #if it is a closing bracket:
            if s[i] in valid.keys():
                #check if the value in the stack is the correct pair
                if len(stack) != 0:
                    if valid[s[i]] == stack[-1]:
                        stack.pop()
                    #if there is no matching pair return False
                    else:
                        return False
                else: 
                    return False


        if len(stack)!= 0:
            return False
        return True






        

