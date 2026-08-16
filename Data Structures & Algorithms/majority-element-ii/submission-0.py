class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        p= sorted(nums)
        for i in range(0,(len(p)-2)):
            if p[i]==p[i+1]==p[i+2] :
                return [p[i]]
        return []