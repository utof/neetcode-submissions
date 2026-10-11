class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            midindex = (r+l)//2
            val = nums[midindex]
            if val == target:
                return midindex
            elif val < target:
                l = midindex + 1
                continue
            r = midindex - 1
        
        return -1 if nums[l] != target else l 