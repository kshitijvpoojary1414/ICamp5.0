class TwoDimensionalArray :
  def rotateImage(self, matrix) :
    l = 0
    r = len(matrix)-1

    while l < r :
        for i in range(r - l) :
            top, bottom = l, r 
            topLeft = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom-i][l]
            matrix[bottom-i][l] = matrix[bottom][r - i]
            matrix[bottom][r-i] = matrix[top+i][r]
            matrix[top+i][r] = topLeft

        l += 1
        r -= 1 

    return matrix

  def zigZag(self, matrix) :
    row = 0
    col = 0 
    i = 0
    up = True 

    while i < len(matrix) * len(matrix[0]) :
      result.append(matrix[row][col])
      if (row == 0 or row <= len(matrix)-1) and col != len(matrix[0]) :
        col += 1
        result.append(matrix[row][col])
        up = not up 
      
      if (col == 0 or col <= len(matrix[0])) :
        row + 1 
        result.append(matrix[row][col])
        up = not up 


      if row ==len(matrix) and col == len(matrix[0]) :
        break 

      if up :
        row -= 1
        col += 1
      else :
        row += 1
        col -= 1

  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      layers = int(len(matrix) /2 )
      left, right =0, len(matrix[0]) - 1
      up, down = 0, len(matrix) - 1
      result = []

      while left <= right and up <= down :
          print(left, right, up, down)
          for i in range(left,right + 1) :
              result.append(matrix[up][i])
          
          for i in range(up + 1, down + 1) :
              result.append(matrix[i][right])

          if up != down : 
              for i in range(right-1, left - 1,-1) :
                  result.append(matrix[down][i])

          if left != right :
              for i in range(down-1, up , -1) :
                  result.append(matrix[i][left])

          left += 1
          right -= 1
          up += 1
          down -= 1

      return result
        