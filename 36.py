# -*- coding = utf-8 -*-
# @Time : 11/9/2023 11:33 AM
# @Author : Lauren
# @File : 36.py
# @Software : PyCharm

# below is the simplified version of checking duplicate elements
import collections


def containDuplicate(list):
    sublist = []
    for i in range(len(list)):
        if list[i] != ".":
            if list[i] not in sublist:
                sublist.append(list[i])
            else:
                return False
    return True


def isValidSudoku(board: List[List[str]]) -> bool:
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) # create a defaultdic with
    # default values as sets
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r//3, c//3)]):
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    return True


def main():
    board1 = [["5","3",".",".","7",".",".",".","."]
             ,["6",".",".","1","9","5",".",".","."]
             ,[".","9","8",".",".",".",".","6","."]
             ,["8",".",".",".","6",".",".",".","3"]
             ,["4",".",".","8",".","3",".",".","1"]
             ,["7",".",".",".","2",".",".",".","6"]
             ,[".","6",".",".",".",".","2","8","."]
             ,[".",".",".","4","1","9",".",".","5"]
             ,[".",".",".",".","8",".",".","7","9"]]

    board2 = [["8","3",".",".","7",".",".",".","."]
             ,["6",".",".","1","9","5",".",".","."]
             ,[".","9","8",".",".",".",".","6","."]
             ,["8",".",".",".","6",".",".",".","3"]
             ,["4",".",".","8",".","3",".",".","1"]
             ,["7",".",".",".","2",".",".",".","6"]
             ,[".","6",".",".",".",".","2","8","."]
             ,[".",".",".","4","1","9",".",".","5"]
             ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board1))
    print(isValidSudoku(board2))

if __name__ == "__main__":
    main()
