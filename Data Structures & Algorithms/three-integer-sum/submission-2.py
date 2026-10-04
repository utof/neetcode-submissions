class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        solutions = []
        prev = None
        for index, number in enumerate(nums_sorted):
            left = index + 1
            right = len(nums_sorted) - 1
            while left < right:
                sum = number + nums_sorted[left] + nums_sorted[right]
                if sum < 0:
                    left += 1
                    continue
                elif sum > 0:
                    right -= 1
                    continue
                solutions.append([number, nums_sorted[left], nums_sorted[right]])
                break

        return solutions

        