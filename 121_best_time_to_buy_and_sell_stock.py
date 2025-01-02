class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pmax = 0
        start = 0
        stop = 0
        ## loop trough prices
        for idx,price in enumerate(prices):
            ## if we find new low then reset valeey and peak
            if price < prices[start] :
                start = idx
                stop = idx
            ## if we find new high then update peak            
            if price > prices[stop]:
                stop = idx
                ## compare with previous max profit
                pmax = max(pmax, price - prices[start])

        return pmax

## Simplistic solution with O(n) time complexity 36ms