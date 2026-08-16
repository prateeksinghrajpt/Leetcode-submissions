class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        p= sorted(nums)
        res = []
        threshold = len(p) // 3
        i = 0
        while i < len(p):
            count = 1
            while i + 1 < len(p) and p[i] == p[i+1]:
                count += 1
                i += 1
            if count > threshold:
                res.append(p[i])
            i += 1
        return res