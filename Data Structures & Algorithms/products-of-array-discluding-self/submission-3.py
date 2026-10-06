class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, res= [1]*len(nums),[1]*len(nums), []
        res1, res2= 1,1
        for n in range(1,len(nums)):
            res1*=nums[n-1]
            prefix[n]=res1
        
        for j in range(len(nums)-2,-1,-1):
            res2*=nums[j+1]
            postfix[j]=res2

        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
        return res