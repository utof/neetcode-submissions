class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        midpoint_index = 0
        while l < r:
            midpoint_index = (r + l)//2
            if target < matrix[midpoint_index][0]:
                r = midpoint_index - 1
                continue
            elif target > matrix[midpoint_index][-1]:
                l = midpoint_index + 1
                continue
            else:
                break
        midpoint_index = (r + l)//2
        l = 0
        r = len(matrix[r]) - 1
        while l < r:
            midpoint = (r + l)//2
            if target < matrix[midpoint_index][midpoint]:
                r = midpoint - 1
                continue
            if target > matrix[midpoint_index][midpoint]:
                l  = midpoint + 1
                continue
            return True 
        return False if matrix[midpoint_index][r] != target else True
            

        