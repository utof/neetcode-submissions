class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        def suff(i):
            if i == len(nums) - 2:
                return nums[len(nums) - 1]
            if i == len(nums) - 1:
                return 1
            return suff(i + 1) * nums[i + 1]

        def pref(i):
            if i == 0:
                return 1
            if i == 1:
                return nums[0]
            return pref(i - 1) * nums[i - 1]

        final_arr = [0] * len(nums)
        for i in range(len(nums)):
            prefix[i] = pref(i)
            suffix[i] = suff(i)
            final_arr[i] = pref(i) * suff(i)
        return final_arr
