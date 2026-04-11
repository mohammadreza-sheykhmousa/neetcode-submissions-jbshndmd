class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #l-buyday, r-sellday
        maxb = 0
        while r < len(prices):
            #dosomting
            if prices[r] > prices[l]:
                currb = prices[r] - prices[l]
                maxb = max(maxb, currb)
            else:
                l = r            
            r += 1
        return maxb