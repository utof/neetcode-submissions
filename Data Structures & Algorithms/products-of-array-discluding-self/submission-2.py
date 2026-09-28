class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        final_arr = []
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            # print(prefix[i], prefix[i-1], nums[i-1])
            # suffix[i] = suffix[i+1] * nums[len(nums)-i]
            # final_arr.append(suffix[i]*prefix[i])

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            final_arr.append(suffix[i]*prefix[i])
        # print(suffix, "\n", prefix, "\n", final_arr)
        return final_arr