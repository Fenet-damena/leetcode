# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def numadj(self,board,x,y):
        num_m = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i >=0 and i< len(board) and j >= 0 and j <len(board[0]) and board[i][j] == "M":
                    num_m += 1     
        return num_m

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    
        if not board:
            return board
        x,y = click
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            num_m = self.numadj(board, x, y)
            if num_m > 0:
                board[x][y] = str(num_m)
            else:
                board[x][y] = "B"
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if i >=0 and i< len(board) and j >= 0 and j <len(board[0]) and board[i][j] != "B":
                            self.updateBoard(board,[i,j])
        return board

