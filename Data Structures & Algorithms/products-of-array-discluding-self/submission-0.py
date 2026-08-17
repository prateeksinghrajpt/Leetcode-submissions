class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=1
        ans=[]
        for num in nums:
            res *= num
        for i in range(len(nums)):
            if nums[i] !=0:
                ans.append(res//nums[i])
        return ans 

        

        