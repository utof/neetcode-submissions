class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = [-1]*len(arr)
        for i in range(len(arr) - 2, -1, -1):
            greatest[i] = max(greatest[i+1], arr[i+1])
        return greatest