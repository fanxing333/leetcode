from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        pre_mul = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * pre_mul
            pre_mul = pre_mul * nums[i]

        return res


if __name__ == "__main__":
    input = [1,2,3,4]

    s = Solution()
    print(s.productExceptSelf(input))
