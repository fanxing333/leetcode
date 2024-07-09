from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        if k == 0:
            return 
        n = len(nums)

        import math
        gcd = math.gcd(n, k)
        max_bias = n / gcd

        print(max_bias)

        swapped_idx = 0
        swapped_num = nums[swapped_idx]

        test = [swapped_idx]
        for i in range(1, n+1):
            swapped_idx = (swapped_idx + k) % n
            t = swapped_num
            swapped_num = nums[swapped_idx]
            nums[swapped_idx] = t

            if i % max_bias == 0:
                swapped_idx += 1
                swapped_num = nums[swapped_idx]

            print("next swap idx: ", swapped_idx, nums)
            test.append(swapped_idx)

        print(test)


    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return 
        n = len(nums)

        swapped_idx = n-k
        swapped_num = nums[swapped_idx]

        max_bias = n
        if n % k == 0:
            max_bias = n / k

        for i in range(1, n):
            if i % max_bias == 0:
                swapped_idx += 1
            swapped_idx = (swapped_idx + k) % n
            t = swapped_num
            swapped_num = nums[swapped_idx]
            nums[swapped_idx] = t
            print(swapped_idx, nums)

        nums[(swapped_idx + k) % n] = swapped_num

        

if __name__ == "__main__":
    input = [1,2,3,4,5,6,7]
    k = 3

    input = [-1,-100,3,99]
    k = 2

    input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
    k = 23

    s = Solution()
    print(s.rotate(input, k))
    print(input)
