class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        # position, speed = map(list, zip(*pairs))
        time_to_end = [(target - p)/s for p, s in pairs]
        stack = []
        for i in range(len(pairs) - 1, -1, -1):
            if not stack or time_to_end[i] > stack[-1]:
                stack.append(time_to_end[i])
        return len(stack) 

