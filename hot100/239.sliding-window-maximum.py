from typing import List

class Solution:
    """
    单调队列真是一种让人感到五味杂陈的数据结构，它的维护过程更是如此.....就拿此题来说，队头最大，往队尾方向单调......有机会站在队头的老大永远心狠手辣，当它从队尾杀进去的时候，如果它发现这里面没一个够自己打的，它会毫无人性地屠城，把原先队里的人头全部丢出去，转身建立起自己的政权，野心勃勃地准备开创一个新的王朝.....这时候，它的人格竟发生了一百八十度大反转，它变成了一位胸怀宽广的慈父！它热情地请那些新来的“小个子”们入住自己的王国......然而，这些小个子似乎天性都是一样的——嫉妒心强，倘若见到比自己还小的居然更早入住王国，它们会心狠手辣地找一个夜晚把它们通通干掉，好让自己享受更大的“蛋糕”；当然，遇到比自己强大的，它们也没辙，乖乖夹起尾巴做人。像这样的暗杀事件每天都在上演，虽然王国里日益笼罩上白色恐怖，但是好在没有后来者强大到足以干翻国王，江山还算能稳住。直到有一天，闯进来了一位真正厉害的角色，就像当年打江山的国王一样，手段狠辣，野心膨胀，于是又是大屠城......历史总是轮回的。
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        from collections import deque
        monotonic_queue = deque()

        for i in range(k):
            while monotonic_queue and nums[i] > nums[monotonic_queue[-1]]:
                monotonic_queue.pop()
            monotonic_queue.append(i)

        res.append(nums[monotonic_queue[0]])

        for right in range(k, len(nums)):
            # 双端队列，该左弹出的左弹出，该右弹出的右弹出
            if right - k + 1> monotonic_queue[0]:
                monotonic_queue.popleft()

            while monotonic_queue and nums[right] > nums[monotonic_queue[-1]]:
                monotonic_queue.pop()
            monotonic_queue.append(right)

            # 将双端队列的第一个加入到 res
            res.append(nums[monotonic_queue[0]])
            
        return res
    

    """
    超时
    """
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        res = []
        left, right = 0, k - 1
        if right > len(nums) - 1:
            return [max(nums)]
        max_num = max(nums[:k])
        max_idx = nums[:k].index(max_num)

        res.append(max_num)
        
        # second_max_num = max(nums[max_idx+1:k])
        # second_max_idx = nums[max_idx+1:k].index(second_max_num)

        while right < len(nums)-1:
            left += 1
            right += 1

            if left > max_idx:
                # 更新 max 和 second_max
                max_num = max(nums[left: right+1])
                max_idx = nums[left: right+1].index(max_num)
            else:
                if nums[right] > max_num:
                    max_num = nums[right]
                    max_idx = right
                
            res.append(max_num)
            


        return res

if __name__ == "__main__":
    input = [1,3,-1,-3,5,3,6,7]
    k = 3

    s = Solution()
    print(s.maxSlidingWindow(input, k))
