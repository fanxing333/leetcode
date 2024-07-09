from typing import List

class Solution:
    """
    如何只使用常数级别的空间复杂度？
    提示：只在原数组中进行操作
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        


    """
    First AC Version
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        pos = [0] * n

        for i in range(n):
            if nums[i] > 0 and nums[i] < n+1:
                pos[nums[i]-1] = nums[i]

        for i in range(n):
            if pos[i] == 0:
                return i+1
            
        return n + 1

if __name__ == "__main__":
    input = [3,4,-1,1]

    s = Solution()
    print(s.firstMissingPositive(input))
