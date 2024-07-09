class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        hashtable = {}
        for i, num in enumerate(nums):
            if num in hashtable:
                continue
            else:
                hashtable[num] = 1

            if num + 1 in hashtable:
                hashtable[num] = hashtable[num+1] + 1
            
            if num - 1 in hashtable:
                least_num = num - 1
                while least_num in hashtable:
                    least_num = least_num - 1
                
                hashtable[least_num+1] = hashtable[least_num+1] + hashtable[num]
            

        return max(hashtable.values())
    
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                while current_num + 1 in num_set:
                    current_num += 1
                
                longest = max(current_num - num, longest)

        return longest

if __name__ == "__main__":
    nums = []
    s = Solution()
    print(s.longestConsecutive(nums))