class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        leaders=[]
        maxCount=1
        if nums==[]:
            return 0
        for n in s:
            if n-1 not in s:
                leaders.append(n)
        for n in leaders:
            count=1
            j=n
            while j+1 in s:
                count+=1
                j+=1
            if count>maxCount:
                maxCount=count
        return maxCount

