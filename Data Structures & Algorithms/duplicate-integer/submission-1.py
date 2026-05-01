class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_Duplicate_set=set(nums)
        if len(non_Duplicate_set) < len(nums):
            return True
        else:
            return False
