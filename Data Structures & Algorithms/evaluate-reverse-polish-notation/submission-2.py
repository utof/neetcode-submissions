class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            match i:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    stack.append(stack[-2] / stack.pop())
                    stack.pop()
                case "-":
                    stack.append(stack[-2] - stack.pop())
                    stack.pop()
                case _:
                    stack.append(int(i))
        return stack[-1]

                        


