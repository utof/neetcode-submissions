class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parendict = {}
        parendict["]"] = "["
        parendict[")"] = "("
        parendict["}"] = "{"
 
        for i,j in enumerate(s):
            stack.append(j)
            if len(stack) > 1 and j in parendict:
                if stack[-2] == parendict[j]:
                    stack.pop()
                    stack.pop()
                else:
                    return False
        return True if len(stack) % 2 == 0 else False