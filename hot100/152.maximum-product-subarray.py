from typing import List

class Solution:
    """
    max_product[i] 表示为 以 nums[i] 结尾的最大乘积
    min_product[i] 表示为 以 nums[i] 结尾的最小乘积
    max_product[i] = max(max_product[i - 1] * nums[i], min_product[i - 1] * nums[i], nums[i])
    min_product[i] = min(max_product[i - 1] * nums[i], min_product[i - 1] * nums[i], nums[i])
    """
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[:]
        min_product = nums[:]

        for i in range(1, len(nums)):
            max_product[i] = max(max_product[i - 1] * nums[i], min_product[i - 1] * nums[i], nums[i])
            min_product[i] = min(max_product[i - 1] * nums[i], min_product[i - 1] * nums[i], nums[i])

        return max(max_product)

if __name__ == "__main__":
    input = [2,3,-2,4]
    input = [2,-5,-2,-4,3]

    s = Solution()
    print(s.maxProduct(input))
