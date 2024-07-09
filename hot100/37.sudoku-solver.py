from typing import List

class Board:
    def __self__(self, board: List[List[str]]):
        self.board = self.parse_board(board)

    def parse_board(self, board):
        pass

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_block_id(index):
            row = index // 9
            col = index % 9
            
            block_row = row // 3
            block_col = col // 3
            block_id = block_row * 3 + block_col
            return block_id
        
        def get_used_number_from_block(block_id):
            start_row = (block_id // 3) * 3
            start_col = (block_id % 3) * 3
            indices = set()
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    indices.add(row * 9 + col)
            
            return set([pinned_table[i] for i in (indices & set(pinned_table.keys()))])

        def get_used_number_from_row(index):
            row = index // 9
            indices = set(range(row * 9, row * 9 + 9))

            return set([pinned_table[i] for i in (indices & set(pinned_table.keys()))])


        def get_used_number_from_col(index):
            col = index % 9
            indices = set(range(col, 8 * 9 + col, 9))

            return set([pinned_table[i] for i in (indices & set(pinned_table.keys()))])
        
        action_stack = []
        res_action_stack = []
        
        def do(step):
            action_stack.append(step)
            index, value = step
            pinned_table[index] = value
            unpinned_table[index].remove(value)

            res_action_stack.append(unpinned_table[index])

            if len(unpinned_table[index]) == 0:
                del unpinned_table[index]



            pass

        def undo():
            index, value = action_stack.pop()
            del pinned_table[index]
            if index in unpinned_table.keys():
                unpinned_table[index].add(value)
            else:
                unpinned_table[index] = {value}
            
            pass

        def update(index):
            # 1. 当进行一次动作后，刷新一次 unpinned_table 的候选集，如果某个 key 是空集合，则视为一次失败
            # 2. 失败则返回一个信号
            # 函数外部若接收到失败信号，则进行回溯 undo，直到可以选择另一条路
            available_index = set()
            block_id = get_block_id(index)

            # block 内相关的 index
            start_row = (block_id // 3) * 3
            start_col = (block_id % 3) * 3
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    available_index.add(row * 9 + col)

            # row 内相关 index
            row = index // 9
            available_index.union(set(range(row * 9, row * 9 + 9)))
            # col 内相关 index
            col = index % 9
            available_index.union(set(range(col, 8 * 9 + col, 9)))
            # 与 unpinned_table 做交集
            available_index = available_index & unpinned_table.keys()

            for idx in available_index:
                block_id = get_block_id(idx)
                unpinned_table[idx] -= get_used_number_from_block(block_id)
                unpinned_table[idx] -= get_used_number_from_row(idx)
                unpinned_table[idx] -= get_used_number_from_col(idx)
                if len(unpinned_table[idx]) == 0:
                    return 0
                
            return 1

        def get_strategic_step():
            # return (index, number)
            min_possibilities = 9
            strategic_step = (None, None)
            for key, value in unpinned_table.items():
                if len(value) < min_possibilities:
                    min_possibilities = len(value)
                    strategic_step = (key, value)
            
            return strategic_step

        # 1. 获得已确定数的下标列表，获得未确定数的下标列表
        # 2. 获得所有未确定数可能的取值范围
        #       1. 初始化候选集，在候选集里排除 该数所在块内其他已确定的数
        #       2. 排除该数所在行里其他已确定的数
        #       3. 排除该数所在列里其他已确定的数
        # 3. 对未确定的数进行排序，选择可能性最大的一个数中的一个值
        # 4. 更新确定数和未确定数列表
        # 5. 如果无解，则回溯

        pinned_table = {}
        unpinned_table = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    unpinned_table[i * 9 + j] = set([str(i) for i in range(9)])
                else:
                    pinned_table[i * 9 + j] = board[i][j]
        
        # update unpinned_table
        for idx in unpinned_table.keys():
            block_id = get_block_id(idx)
            unpinned_table[idx] -= get_used_number_from_block(block_id)
            unpinned_table[idx] -= get_used_number_from_row(idx)
            unpinned_table[idx] -= get_used_number_from_col(idx)
            print(idx, unpinned_table[idx])
        
        while len(unpinned_table.keys()) > 0:
            # 1. 选择符合策略的一步
            # 2. do
            # 3. 更新候选集
            # 4. 如果接收到失败信号，则回溯（undo）到最小重复点
            step = get_strategic_step()
            print(step)
            do(step)

            while update(step[0]) == 0:
                undo()



        

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

    s = Solution()
    s.solveSudoku(board)
    print(board)
