class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            nums = set()
            for j in range(0,9):
                if board[i][j]=='.':
                    continue
                if int(board[i][j]) > 9:
                    return False
                if board[i][j] in nums:
                    return False
                nums.add(board[i][j])
            nums = set()
            for j in range(0,9):
                if board[j][i]=='.':
                    continue
                if int(board[j][i]) > 9:
                    return False
                if board[j][i] in nums:
                    return False
                nums.add(board[j][i])
        for i in range(0,9,3):
            for j in range(0,9,3):
                nums = set()
                for k in range(0,3):
                    for l in range(0,3):
                        if board[i+k][j+l]=='.':
                            continue
                        if int(board[i+k][j+l]) > 9:
                            return False
                        if board[i+k][j+l] in nums:
                            return False
                        nums.add(board[i+k][j+l])

        return True