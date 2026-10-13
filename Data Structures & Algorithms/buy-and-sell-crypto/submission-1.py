class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0, 1
        currMax=0

        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                currMax=max(currMax,prices[r]-prices[l])
            r+=1
        return currMax