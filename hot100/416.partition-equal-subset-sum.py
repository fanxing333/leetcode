from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        
        all_sum = sum(nums)
        if all_sum % 2 != 0:
            return False
        else:
            target = all_sum // 2

        if max(nums) > target:
            return False

        # 题目转化为 在数组中选择哪些数可以使其和为 sub_sum
        dp = [[True] + [False] * target for _ in range(n)]
        dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(target + 1):
                if j == nums[i]:
                    dp[i][j] = True
                elif j > nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]


if __name__ == "__main__":
    input = [1,5,11,5]
    input = [9,5]

    s = Solution()
    print(s.canPartition(input))
