from typing import List

class Solution:
    """
    返回最长的严格递增子序列的长度
    维护 length 数组
    length[i] 表示到第 i 个数字结尾的最长递增子序列的长度
    length[i] = max(dp[j]) + 1, 其中 j < i 且 nums[j] < nums[i]

    return max(dp)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        length[0] = 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    length[i] = max(length[i], length[j] + 1)
        
        return max(length)


if __name__ == "__main__":
    input = [10,9,2,5,3,7,101,18]

    s = Solution()
    print(s.lengthOfLIS(input))
