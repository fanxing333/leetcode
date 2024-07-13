from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visit = [[False for _ in range(n)] for _ in range(m)]

        exist = False
        def backtrace(first=0, row=0, col=0):
            nonlocal exist            
            if first == len(word):
                exist = True
                return
            
            if row < 0 or row > m - 1:
                return
            
            if col < 0 or col > n - 1:
                return
            
            if not visit[row][col]:
                if board[row][col] == word[first]:
                    visit[row][col] = True
                    backtrace(first+1, row, col+1)
                    backtrace(first+1, row, col-1)
                    backtrace(first+1, row+1, col)
                    backtrace(first+1, row-1, col)
                    visit[row][col] = False

        for i in range(m):
            for j in range(n):
                if exist:
                    return exist
                backtrace(row=i, col=j)

        return exist

if __name__ == "__main__":
    input = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"

    input = [["a","b"]]
    word = "ba"

    s = Solution()
    print(s.exist(input, word))
