from typing import List

class Solution:
    """
    还是循环置换的思想
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        swap_bias = n - 1
        loop_time = n // 2
        for i in range(loop_time):
            row = i
            col = i

            for j in range(swap_bias):
                print((row, col + j), (row + swap_bias - j, col), (row + swap_bias, col + swap_bias - j), (row + j, col + swap_bias))
                t = matrix[row][col + j]
                matrix[row][col + j] = matrix[row + swap_bias - j][col]
                matrix[row + swap_bias - j][col] = matrix[row + swap_bias][col + swap_bias - j]
                matrix[row + swap_bias][col + swap_bias - j] = matrix[row + j][col + swap_bias]
                matrix[row + j][col + swap_bias] = t

            swap_bias -= 2
            

        


if __name__ == "__main__":
    input = [[1,2,3],[4,5,6],[7,8,9]]

    s = Solution()
    print(s.rotate(input))
    print(input)
