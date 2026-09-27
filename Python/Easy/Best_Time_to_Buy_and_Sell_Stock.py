class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num=float("inf")
        profit=0
        for e in prices:
            if e<min_num:
                min_num=e
            else:
                profit=max(profit, e-min_num)
        return profit
