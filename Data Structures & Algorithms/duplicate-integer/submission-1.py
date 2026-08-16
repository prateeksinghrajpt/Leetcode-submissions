class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        p= sorted(nums)
        for i in range(len(p) - 1):
            if p[i]== p[i+1]:
                return True
        return False