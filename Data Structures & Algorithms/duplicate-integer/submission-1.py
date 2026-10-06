class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={} #val : index
        for i,n in enumerate(nums):
            if n in mp:
                return True
            mp[n]=i
        return False