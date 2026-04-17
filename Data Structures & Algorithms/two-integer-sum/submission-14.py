class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        progressiveMap = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in progressiveMap:
                return [progressiveMap[need], i]
            progressiveMap[num] = i


        

        