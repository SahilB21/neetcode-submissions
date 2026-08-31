class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        indices = []
        for i, num in enumerate(nums):
            if target - num in numbers:
                if i < numbers[target-num]:
                    indices = [i, numbers[target-num]]
                else:
                    indices = [numbers[target-num], i]
                return indices
            numbers[num] = i
        return indices