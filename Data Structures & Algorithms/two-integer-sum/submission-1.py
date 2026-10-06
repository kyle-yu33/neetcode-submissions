class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {} #val : index
        for i,n in enumerate(nums): 
            diff = target - n
            if diff in mp:
                return [mp[diff],i]
            mp[n]=i