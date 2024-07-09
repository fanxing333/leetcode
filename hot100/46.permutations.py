from typing import List

class Solution:
    """
    回溯的递归实现
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        output = []

        def backtrace(first=0, visit=[False] * n):
            # 退出条件
            if first == n:
                res.append(output[:])
            # 
            for i in range(n):

                if not visit[i]:
                    visit[i] = True
                    output.append(nums[i])

                    # 进入递归
                    backtrace(first+1, visit)

                    # 结束递归的回退
                    output.pop()
                    visit[i] = False

        backtrace(0)

        return res
    

    """
    First AC Version
    """
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []
        action_stack = [[i for i in nums]]

        r = []
        while len(action_stack) > 0:
            # 1. action
            # 2. trace back
            action_set = action_stack[-1]  # 如何确保 action_set 不为空？
            action = action_set.pop()
            r.append(action)

            if len(r) == len(nums):
                res.append(r)
                while len(action_stack) > 0 and len(action_stack[-1]) == 0:
                    action_stack.pop()
                r = r[:len(action_stack)-1]
            else:
                action_stack.append(list(set(nums) - set(r)))

        return res

if __name__ == "__main__": 
    input = [1,2,3,4]

    s = Solution()
    print(s.permute(input))
