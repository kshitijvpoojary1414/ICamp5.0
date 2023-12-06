class SodokuSolver :
  def solveSodoku(self, board) :
    self.helper(0,0,board, BoardChecker(board))
    return board

  def helper(self, i, j, board, checker) :
    if i == len(board) :
      return True 

    nextPair = self.next(i,j)

    if board[i][j] != "." :
      return self.helper(nextPair(i), nextPair(j), board) 

    for num in range(1,10) :
      if checker.canPlace(i,j,num) :
        checker.place(i,j,num)
        if self.helper(nextPair(i), nextPair(j), board, checker) :
          return True 
        checker.remove(i,j,num)
        board[i][j] = "."

  def next(self,i,j) :
    if j == 9 :
      return (i + 1, 0)
    return (i, j +1)
class BoardChecker :
  def __init__(self, board) :
    self.row = [[False for i in range(9)] for i in range(9)]
    self.col = [[False for i in range(9)] for i in range(9)]
    self.box = [[False for i in range(9)] for i in range(9)]

    for i in range(9) :
      for j in range(9) :
        num = board[i][j]

        if num != "*" :
          num = int(num)
          self.row[i][num] = True
          self.col[j][num] = True
          self.box[self.boxNumber(i,j)][num] = True

  def canPlace(self, i, j, num) :
    if self.row[i][num] :
      return False 
    if self.col[j][num] :
      return False 
    if self.box[self.boxNumber(i,j)][num] :
      return False 

    return True 

  def place(self, i, j, num ) :
    self.row[i][num] = True
    self.col[j][num] = True
    self.box[self.boxNumber(i, j)][num] = True
  
  def remove(self,i,j,num) :
    self.row[i][num] = False
    self.col[j][num] = False
    self.box[self.boxNumber(i, j)][num] = False

  def boxNumber(self, i, j) :
    return (i//3)*3 + j//3