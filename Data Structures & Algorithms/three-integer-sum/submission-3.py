class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        solutions = []
        for index, number in enumerate(nums_sorted):
            if index > 0 and number == nums_sorted[index-1]:
                continue
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
                else:
                    solutions.append([number, nums_sorted[left], nums_sorted[right]])
                    left += 1
                    while nums_sorted[left] == nums_sorted[left -1] and left < right:
                        left +=1

        return solutions

        