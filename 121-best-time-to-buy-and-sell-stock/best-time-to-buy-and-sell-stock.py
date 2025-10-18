class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minn = float('inf')
        max_profit = 0
        for price in prices:
            if price < minn:
                minn = price
            elif price - minn > max_profit:
                max_profit = price - minn
        return  max_profit
       


        

        