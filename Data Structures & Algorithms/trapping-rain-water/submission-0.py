class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = [0]*len(height), [0]*len(height)
        final_val = 0
        left_max[0], right_max[-1] = height[0], height[-1]
        for index in range(1, len(height)-1):
            left_max[index] = max(left_max[index-1], height[index])
        
        for index in range(len(height) - 2, 0, -1):
            right_max[index] = max(right_max[index+1], height[index])
        for i in range(len(height)):
            summ = min(left_max[i], right_max[i]) - height[i]
            final_val += summ if summ > 0 else 0
        return final_val
        
        
