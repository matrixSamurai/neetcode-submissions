class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # in python, a list is a stack
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack) != 0:
                poppedElement = stack.pop()
                if poppedElement == '(' and c != ')':
                    return False
                if poppedElement == '[' and c != ']':
                    return False
                if poppedElement == '{' and c != '}':
                    return False
            else:
                return False
        
        if len(stack) == 0:
            return True
        
        return False

                

        