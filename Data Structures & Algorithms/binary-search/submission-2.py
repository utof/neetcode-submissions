class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = (len(nums) - 1)//2
        diff = i
        while nums[i] != target:
            if diff == 0:
                return -1
            if nums[i] < target:
                i += diff
            else:
                i -= diff
            if not (0 <= i < len(nums) - 1):
                return -1
            diff = diff//2
        return i