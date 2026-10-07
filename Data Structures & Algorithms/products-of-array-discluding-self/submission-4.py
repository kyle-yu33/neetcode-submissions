class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        p,pf = 1,1

        for i in range(len(nums)):
            res[i]=p
            p*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=pf
            pf*=nums[i]
        return res