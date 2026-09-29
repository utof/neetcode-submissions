class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_squares = {}
        rows_set = {}
        col_set = {}
        def check_sudoku(board):
            for row_index, row in enumerate(board):
                for cell_index, cell in enumerate(row):
                    curr_square = cell_index//3 + row_index//3 * 3
                    # but if cell is in curr square then return false, how???
                    if cell == '.':
                        continue
                    if curr_square in set_squares and (cell in set_squares.get(curr_square, set())
                        or cell in rows_set.get(row_index, set()) 
                        or cell in col_set.get(cell_index, set())):
                        return False
                    set_squares.setdefault(curr_square, set()).add(cell)
                    rows_set.setdefault(row_index, set()).add(cell)
                    col_set.setdefault(cell_index, set()).add(cell) 
            return True
        return check_sudoku(board)