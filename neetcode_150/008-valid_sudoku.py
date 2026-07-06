# Problem: Valid Sudoku
# Difficulty: Medium
# Link NeetCode: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150
# Link LeetCode: https://leetcode.com/problems/valid-sudoku/description/

from typing import List

# Approach: Use data structure set of each row, column, square
# Time Complexity: O(n * m)

class Solution:
    def isValidCol(self, x: int, y:int) -> bool:
        if (self.board[x][y] in self.ls_col[y]):
            return False
        self.ls_col[y].add(self.board[x][y])
        return True
    
    def isValidRow(self, x: int, y: int) -> bool:
        if (self.board[x][y] in self.ls_row[x]):
            return False
        self.ls_row[x].add(self.board[x][y])
        return True
    
    def isValidSqu(self, x: int, y: int) -> bool:
        val = (x//3)*3 + (y//3)
        if (self.board[x][y] in self.ls_squ[val]):
            return False
        self.ls_squ[val].add(self.board[x][y])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        self.ls_row = collections.defaultdict(set)
        self.ls_col = collections.defaultdict(set)
        self.ls_squ = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "." or (self.isValidRow(i, j) and self.isValidCol(i, j) and self.isValidSqu(i, j)):
                    continue
                else:
                    return False
        return True

