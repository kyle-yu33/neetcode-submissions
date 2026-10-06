class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} #map integer to occurences 
        freq=[[]for n in range(len(nums)+1)]

        for i in nums:
            count[i]=1+count.get(i,0)
        for n,c in count.items():
            freq[c].append(n)
        
        res=[]
        for n in range(len(freq)-1,0,-1):
            for i in freq[n]:
                res.append(i)
                if (len(res)==k):
                    return res

