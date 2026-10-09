class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        final = [0]*len(temperatures)
        for i, j in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    val = stack[-1]
                    final[stack[-1]] = i - val
                    stack.pop()
            stack.append(i)
        return final