class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(2 * len(nums)):
            if i <= len(nums) - 1:
                lst.append(nums[i])
            else:
                lst.append(nums[i - len(nums)])
        return lst
