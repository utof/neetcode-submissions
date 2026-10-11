class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = (len(nums) - 1)//2
        diff = i
        while nums[i] != target or 0 <= i < len(nums):
            if diff == 0:
                return -1
            if nums[i] < target:
                i += diff
                continue
            i -= diff
            diff = diff//2
        return i
