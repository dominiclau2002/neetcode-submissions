class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack
        stack = []

        #define valid brackets
        opening = "({["
        closing = ")}]"

        #if length is 0 or 1 it cannot be a valid string
        if len(s) == 0 or len(s) == 1:
            return False

        #if the first character is closing then it is definitely invalid
        if s[0] in closing:
            return False

        #iterate through the string 
        for i in range(len(s)):

            #if it is an opening bracket then append it to the stack
            if s[i] in opening:
                stack.append(s[i])
                continue
            elif s[i] in closing:
                #if there is a matching opening bracket to the seen closed bracket:
                if s[i] == ")" and len(stack) != 0  and stack[-1] == "(":
                    #pop the opening bracket from the stack
                    stack.pop()

                elif s[i] == "]" and len(stack) != 0 and stack[-1] == "[":
                    stack.pop()

                elif s[i] == "}" and len(stack) != 0 and stack[-1] == "{":
                    stack.pop()
                
                else:
                    return False

                
                



        #if the stack is not empty, it means that the string is not valid
        print(stack)
        if stack:
            return False
        return True

