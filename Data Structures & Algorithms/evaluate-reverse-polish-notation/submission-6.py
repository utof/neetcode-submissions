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
                    result = stack[-2] // stack.pop()
                    stack.pop()
                    stack.append(result)
                case "-":
                    print(stack[-2], stack[-1])
                    result = stack[-2] - stack.pop()
                    stack.pop()
                    stack.append(result)
                case _:
                    stack.append(int(i))
        print(stack)
        return stack[-1]

                        


