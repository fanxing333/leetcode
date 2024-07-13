from typing import List

class Solution:
    """
    返回最小跳跃次数
    count[i] 表示从 0 跳到第 i 个下标所需要的最小次数
    """
    def jump(self, nums: List[int]) -> int:
        count = [-1] * len(nums)

        count[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if i + j < len(nums):
                    if count[i + j] < 0:
                        count[i + j] = count[i] + 1
                        
        return count[-1]

            


if __name__ == "__main__":
    input = [2,3,1,1,4]

    s = Solution()
    print(s.jump(input))
