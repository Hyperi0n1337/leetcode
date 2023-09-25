#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        result = 0
        for p in prices:
            minPrice = min(minPrice, p)
            result = max(result, p - minPrice)
        return result
# @lc code=end

