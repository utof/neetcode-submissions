class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l - r >= 1:
            midindex = (r+l)//2
            val = nums[midindex]
            if val == target:
                return midindex
            elif val < target:
                l = midindex
                continue
            r = midindex
            
        return -1 