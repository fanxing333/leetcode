from typing import List


class Solution:
    def trap_2(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            # 如果能确定 left 装水容积，left ++
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            # 如果能确定 right 装水容积，right --
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans
    

    def trap_dp(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        leftMax, rightMax = height.copy(), height.copy()
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], leftMax[i])
        
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], rightMax[i])
        
        sum = 0
        for idx in range(len(height)):
            sum += min(leftMax[idx], rightMax[idx]) - height[idx]

        return sum
    
    def trap_1(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        trapped = 0

        left_idx = 0        
        right_idx = 0
        while left_idx < len(height) - 2 and right_idx < len(height) - 1:
        
            right_value = 0
            for i in range(left_idx + 1, len(height)):
                if height[i] > height[left_idx]:
                    right_idx = i
                    right_value = height[right_idx]
                    break
                if height[i] >= right_value:
                    right_idx = i
                    right_value = height[right_idx]
            
            block_trapped = (right_idx - left_idx - 1) * min(height[left_idx], height[right_idx]) - sum(height[left_idx + 1: right_idx])
            trapped += block_trapped

            left_idx = right_idx
            right_idx += 1

        return trapped


if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution()
    print(s.trap_2(height))

