class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxseq = 0
        for number in numset:
            if number - 1 in numset:
                continue
            curr = 1
        
            while number + 1 in numset:
                curr +=1
                number+=1
            if curr > maxseq:
                maxseq = curr
        return maxseq