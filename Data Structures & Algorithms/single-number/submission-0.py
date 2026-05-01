class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xer = 0
        for num in nums:
            xer = num ^ xer
        return xer