class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dct:
                return [dct[diff], i]
            dct[n] = i
