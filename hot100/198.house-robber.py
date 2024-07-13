from typing import List

class Solution:
    """
    维护一个 count 数组，count[i] 表示到第 i 家为止，获得的最大金额
    count[i] = max(count[i - 1], count[i - 2] + nums[i])
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * n
        count[0] = nums[0]
        if n > 1:
            count[1] = max(count[0], nums[1])
        
        for i in range(2, n):
            count[i] = max(count[i - 1], count[i - 2] + nums[i])

        return count[-1]

if __name__ == "__main__":
    input = [1,2,3,1]

    s = Solution()
    print(s.rob(input))
