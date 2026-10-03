class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def threesum(numbers):
            final_arr = []
            for i, subtarget in enumerate(numbers):
                twosum_arr = twosum(numbers, i, subtarget)
                if twosum_arr != None:
                    for solution in twosum_arr:
                        final_arr.append([subtarget, solution[0], solution[1]])

            unique = set()
            for solution in final_arr:
                unique.add(tuple(sorted(solution)))
            
            return [list(x) for x in unique]

        def twosum(numbers, index_of_additional_number, subtarget):
            registry = {}
            final_arr = []
            new_numbers = numbers[index_of_additional_number+1:]
            for index, number in enumerate(new_numbers):
                diff = -subtarget - number
                if diff in registry:
                    final_arr.append([numbers[index+index_of_additional_number+1], numbers[registry[diff]+index_of_additional_number+1]])
                registry[number] = index
            return final_arr
        return threesum(nums)