class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_arr = [0]
        max_dict = {}
        for i in range(len(nums)):
            numsi = nums[i]
            max_dict[numsi] = max_dict.get(numsi, 0) + 1
            if max_dict[numsi] > max_arr[-1]:
                max_arr.append(numsi)
        return max_arr[-k:]
        