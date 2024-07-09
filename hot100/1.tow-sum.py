class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [i, hashtable[target - num]]
            else:
                hashtable[num] = i


    def twoSum_two_dict(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 只有一个有效答案，所以找到即可退出，不需要遍历所有。
        # 目标 时间复杂度 < O(n^2)
        # 
        idx2target = {0: hash(target-nums[0])}
        target2idx = {hash(target-nums[0]):0}
        for i, num in enumerate(nums[1:]):
            if hash(num) in target2idx.keys():
                return [i+1, target2idx[hash(num)]]
            else:
                idx2target[i+1] = hash(target-num)
                target2idx[hash(target-num)] = i+1


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    s = Solution()
    print(s.twoSum(nums, target))