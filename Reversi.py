import check

def othello(board, turn, row, col):
  '''
  returns a Boolean response on whether or not either the black or white piece
  is able to make a particular move on a board that follows the rules of 
  Othello
  
  othello: (listof (listof Str)) Str Nat Nat -> Bool
  Requires:
    The length of the outer list is 8 
    The length of each inner list is 8
    Each string is '', 'B', or 'W'.
    
  
  Examples:
    othello(board, 'B', 3, 0) => True
    othello(board, 'W', 3, 0) => False
    othello(board2, 'W', 1, 2) => False
  
  '''
  
  if turn == 'B':
    opp = 'W'
  if turn == 'W':
    opp = 'B'
  
  ## if the board already has a piece on it 
  if board[row][col] != '':
    return False 
    
  ## horizontal check if move is correct
  elif row-1 in range(8) and board[row-1][col] == opp:
    #checks the above since it checks above row and same column
    for j in range(row):
      if board[j][col] == turn:
        return True
  elif row+1 in range(8) and board[row+1][col] == opp:
    #checks the below since it checks below row and same column
    for j in range(row,8):
      if board[j][col] == turn:
        return True
  
  ## vertical check if move is correct 
  elif col-1 in range(8) and board[row][col-1] == opp:
    for j in range(col):
      if board[row][j] == turn:
        return True
  elif col+1 in range(8) and board[row][col+1] == opp:#checks the below since it checks below row and same column
    for j in range(col,8):
      if board[col][j] == turn:
        return True
  
  
  ## diagonal check if move is correct 
  elif row-1 in range(8) and board[row-1][col-1] == opp:# top left
    for j in range(min(row,col) - 1): 
      if board[row-j][col-j] == turn:
        return True
  elif row+1 in range(8) and board[row+1][col+1] == opp:# bottom right
    for j in range(min(8 - row,8 - col)):
      if board[row+j][col+j] == turn:
        return True
  elif col+1 in range(8) and board[row-1][col+1] == opp:# top right 
    for j in range(min(row,8 - col) - 1):
      if board[row-j][col+j] == turn:
        return True
  elif col-1 in range(8) and board[row+1][col-1] == opp:# bottom left
    for j in range(min(8 - row,col) - 1):
      if board[row+j][col-j] == turn:
        return True
  else:
    return False

##Two sample boards to help with testing.

board = [[ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '', 'B', 'B', 'B',  '',  '',  ''],
         [ '', 'W', 'B', 'W', 'W',  '', 'B',  ''],
         [ '', 'W', 'B', 'W', 'W', 'W', 'W',  ''],
         [ '',  '', 'W', 'W', 'W',  '',  '',  ''],
         [ '',  '',  '', 'W',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  '']]
         
board2 = [[ 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B'],
          [ 'B', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
          [ 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
          [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]

# Examples: 
check.expect("Example 1: Board 2", othello(board2, 'W', 1, 2), False)
check.expect("Example 2: Board 2", othello(board2, 'W', 5, 5), False)
check.expect("Example 3: Board 1", othello(board, 'B', 6, 2), True)

# Tests: 
check.expect("Test 1: Board 1", othello(board, 'B', 5, 2), False)
check.expect("Test 2: Board 1", othello(board, 'B', 6, 2), True)
check.expect("Test 3: Board 1", othello(board, 'B', 5, 6), True)
check.expect("Test 4: Board 1", othello(board, 'B', 4, 7), True)
check.expect("Test 5: Board 1", othello(board, 'B', 6, 2), True)
check.expect("Test 5: Board 1", othello(board, 'B', 6, 4), True)
check.expect("Test 6: Board 1", othello(board, 'B', 6, 5), True)
check.expect("Test 7: Board 1", othello(board, 'B', 7, 2), True)