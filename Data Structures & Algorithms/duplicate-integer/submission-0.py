class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for value in nums:
            if value not in duplicates:
                duplicates.add(value)
            else:
                return True
        return False
        