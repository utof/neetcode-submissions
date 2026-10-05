class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_h = 0
        i = 0
        j = len(heights) - 1 
        while i < j:
            area = min(heights[i], heights[j])*(j-i)
            max_h = max(area, max_h)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_h
        