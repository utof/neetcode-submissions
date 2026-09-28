class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lennums = len(nums)
        lenset = len(set(nums))
        return not (lennums == lenset) 