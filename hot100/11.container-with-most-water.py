from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = (right - left) * min(height[left], height[right])

        tmp_left = left
        tmp_right = right
        if height[left] < height[right]:
            tmp_left += 1
        else:
            tmp_right -= 1
        while tmp_right > tmp_left:
            tmp_water = (tmp_right - tmp_left) * min(height[tmp_left], height[tmp_right])
            if tmp_water > max_water:
                left = tmp_left
                right = tmp_right
                max_water = (right - left) * min(height[left], height[right])

            if height[tmp_left] < height[tmp_right]:
                tmp_left += 1
            else:
                tmp_right -= 1
        
        return max_water


if __name__ == "__main__":
    input = [1,8,6,2,5,4,8,3,7]
    input = [2,3,4,5,18,17,6]

    s = Solution()
    print(s.maxArea(input))