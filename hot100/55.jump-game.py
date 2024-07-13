from typing import List

class Solution:
    """
    方法2
    从前往后遍历，获得可以到达的最远距离
    """
    """
    我们需要找出一条路径，使其移动和为 数组长度 - 1
    查看倒数第二个数能否到达终点
        如果可以，查看倒数第三个数能否到达倒数第二个数
        如果不可以，查看倒数第三个数能否到达终点
    """
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        end_idx = len(nums) - 1
        start_idx = len(nums) - 2

        while start_idx > 0:
            if nums[start_idx] >= end_idx - start_idx:
                end_idx = start_idx
            
            start_idx -= 1
        
        print(start_idx, end_idx)
        if nums[start_idx] >= end_idx - start_idx:
            return True
        else:
            return False

if __name__ == "__main__":
    input = [2,3,1,1,4]

    s = Solution()
    print(s.canJump(input))
