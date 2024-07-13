from typing import List

class Solution:
    """
    在数组中找一个最小值和一个最大值，且最小值要在最大值的左边
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        max_idx, min_idx = 0, 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_idx]:
                min_idx = i
                max_idx = i

            if prices[i] > prices[max_idx]:
                max_idx = i
                profit = prices[max_idx] - prices[min_idx]
                if profit > max_profit:
                    max_profit = profit

        return max_profit


if __name__ == "__main__":
    input = [7,1,5,3,6,4]

    s = Solution()
    print(s.maxProfit(input))
