class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        len = 0
        templen = 0

        for j in nums:
            if j-1 not in s:
                templen = 1
                # j+=1
                while j+templen in s:
                    # j+=1
                    templen+=1
                len = max(len, templen)
        return len
