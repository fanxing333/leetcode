from typing import List

class Solution:
    """
    和 279 思路一致，维护一个 count 数组
    count[0...i] 表示构成 i+1 所需要的兑换的最小次数
    count[i] = min(count[i], count[i - coins[j]])
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort()
        count = [amount + 1] * amount
        for i in range(amount):
            for coin in coins:
                if coin == i + 1:
                    count[i] = 1
                elif coin < i + 1:
                    count[i] = min(count[i], count[i - coin] + 1)
                else:
                    break

        if count[-1] > amount:
            return -1
        else:
            return count[-1]

        
if __name__ == "__main__":
    input = [1, 2, 5]
    amount = 11

    s = Solution()
    print(s.coinChange(input, amount))
