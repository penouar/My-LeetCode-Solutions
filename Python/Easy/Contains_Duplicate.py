class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numy=set(nums)
        if len(numy)==len(nums):
            return False
        return True
